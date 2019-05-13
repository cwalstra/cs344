'''
Created on 22 sty 2018
3D Object Representations for Fine-Grained Categorization
Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei
4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.
@author: mgdak
Additions: cwalstra
'''

'''
This file implements the functions that start and control the training of the model.
'''


from keras import callbacks
from keras.optimizers import SGD, RMSprop
from matplotlib import pyplot as plt
from utilityFunctions import evaluate, readData, readClasses, dataPreprocessing, serializeModel, prepareDataGenerators
from architectures import getVGG16Architecture, getVGG19Architecture, getInceptionV3Architecture, getMyCNN

train_data_dir = 'cars_train'
val_data_dir = 'cars_val'
nb_train_samples = 1043
nb_val_samples = 300

def setLayersToRetrain(model, modelArchitecture):
    if modelArchitecture == 'InceptionV3':
        # we chose to train the top 2 inception blocks, i.e. we will freeze
        # the first 249 layers and unfreeze the rest:
        for layer in model.layers[:249]:
            layer.trainable = False

        for layer in model.layers[249:]:
            layer.trainable = True
    elif modelArchitecture == 'VGG16':
        # train the last conv block
        for layer in model.layers[:15]:
            layer.trainable = False

        for layer in model.layers[15:]:
            layer.trainable = True
    elif modelArchitecture == 'VGG19':
        # train the last conv block
        for layer in model.layers[:17]:
            layer.trainable = False

        for layer in model.layers[17:]:
            layer.trainable = True
    else:
        for layer in model.layers[:5]:
            layer.trainable = False
        for layer in model.layers[5:]:
            layer.trainable = True


def initialTraining(optimizerLastLayer, noOfEpochs, batchSize, savedModelName, train_generator, validation_generator,
                    model, modelArchitecture, lr_decay, learningRate):
    # compile the model and train the top layer only

    rms = RMSprop(decay=lr_decay, lr=learningRate)
    model.compile(optimizer=rms, loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    earlystop = callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, mode='auto')
    history = model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batchSize,
        epochs=noOfEpochs,
        validation_data=validation_generator,
        validation_steps=nb_val_samples // batchSize,
        callbacks=[earlystop])
    plt.plot(history.history['val_acc'], 'r')
    plt.plot(history.history['acc'], 'b')
    plt.title('Performance of model ' + modelArchitecture)
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs No')
    plt.savefig(savedModelName + '_initialModel_plot.png')
    serializeModel(model, savedModelName + "_initialModel")


def finetuningTraining(learningRate, noOfEpochs, batchSize, savedModelName, train_generator, validation_generator,
                       model, lr_decay):
    # we need to recompile the model for these modifications to take effect
    # we use SGD with a low learning rate
    sgd = SGD(lr=learningRate, decay=lr_decay, momentum=0.9, nesterov=True)
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    earlystop = callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, mode='auto')

    # we train our model again (this time fine-tuning the top 2 inception blocks
    # alongside the top Dense layers
    history = model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batchSize,
        epochs=noOfEpochs,
        validation_data=validation_generator,
        validation_steps=nb_val_samples // batchSize,        callbacks=[earlystop])
    plt.clf()
    plt.plot(history.history['val_acc'], 'r')
    plt.plot(history.history['acc'], 'b')
    plt.savefig(savedModelName + '_finalModel_plot.png')
    serializeModel(model, savedModelName + "_finalModel")


def model(learningRate, optimizerLastLayer, noOfEpochs, batchSize, savedModelName, srcImagesDir, labelsFile,
          modelArchitecture, dropoutRate, lr_decay):
    classes, train_generator, validation_generator = prepareDataGenerators(batchSize, srcImagesDir, labelsFile)

    if modelArchitecture == 'VGG16':
        model = getVGG16Architecture(classes, dropoutRate)
    elif modelArchitecture == 'VGG19':
        model = getVGG19Architecture(classes, dropoutRate)
    elif modelArchitecture == "InceptionV3":
        model = getInceptionV3Architecture(classes, dropoutRate)
    else:
        model = getMyCNN(classes, dropoutRate)

    initialTraining(optimizerLastLayer, noOfEpochs, batchSize, savedModelName, train_generator, validation_generator,
                    model, modelArchitecture, lr_decay, learningRate)

    setLayersToRetrain(model, modelArchitecture)


    finetuningTraining(learningRate, noOfEpochs, batchSize, savedModelName, train_generator, validation_generator,
                       model, lr_decay)

    evaluate(learningRate, lr_decay)

