'''
Created on 22 sty 2018
3D Object Representations for Fine-Grained Categorization
Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei
4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.
@author: mgdak
Additions: cwalstra
'''

'''
This file implements the functions necessary to read and write data and evaluate the model.
'''

import os
import scipy.io as sio
from keras.preprocessing.image import ImageDataGenerator
from keras.models import model_from_json
import shutil as sh
from keras.optimizers import SGD

train_data_dir = 'cars_train'
val_data_dir = 'cars_val'
nb_train_samples = 1043
nb_val_samples = 300

def evaluate(learning_rate, lr_decay):
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_datagen.flow_from_directory(
        "/home/cjw44/allCars/car_ims/cars_test",
        target_size=(224, 224),
        batch_size=16,
        class_mode='categorical')

    # load json and create model
    json_file = open("./carRecognition_finalModel" + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("./carRecognition_finalModel" + '.h5')
    print('Loaded model from disk')

    # evaluate loaded model on test data
    sgd = SGD(lr=learning_rate, decay=lr_decay, momentum=0.9, nesterov=True)
    loaded_model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    score = loaded_model.evaluate_generator(test_generator, 3957 / 16, workers=6)
    print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))

# Creates an array with following values: picture name, picture category ID, train/validation label
def readData(matFile):
    content = sio.loadmat(matFile)
    data = [(_[0][0][:], _[5][0][0], _[6][0][0]) for _ in content['annotations'][0]]
    return data


# Creates an array of all classes
def readClasses(matFile):
    content = sio.loadmat(matFile)
    classes = [(_[0]) for _ in content['class_names'][0]]
    return classes


# Movces raw data (pictures) into respective category subfolders with train/validation division
def dataPreprocessing(dataDir, labelsFile):
    data = readData(labelsFile)
    classes = readClasses(labelsFile)
    print("---------------")
    for recData in data:
        if recData[2] == 1:
            # validation set
            os.makedirs(dataDir + "/" + val_data_dir + "/" + classes[recData[1] - 1] + "/", exist_ok=True)
            sh.move(dataDir + "/" + recData[0][8:],
                    dataDir + "/" + val_data_dir + "/" + classes[recData[1] - 1] + "/" + recData[0][8:])
        else:
            os.makedirs(dataDir + "/" + train_data_dir + "/" + classes[recData[1] - 1] + "/", exist_ok=True)
            sh.move(dataDir + "/" + recData[0][8:],
                    dataDir + "/" + train_data_dir + "/" + classes[recData[1] - 1] + "/" + recData[0][8:])  # train set


# serializes the trained model and its weights
def serializeModel(model, fileName):
    # serialize model to JSON
    model_json = model.to_json()
    with open(fileName + ".json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(fileName + ".h5")
    print("Saved model to disk")


def prepareDataGenerators(batchSize, srcImagesDir, labelsFile):
    classes = readClasses(labelsFile)
    # this is the augmentation configuration used for training
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    # this is the augmentation configuration used for testing:
    # only rescaling
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    # this is a generator that will read pictures found in
    # subfolers of 'car_ims_dir/train', and indefinitely generate
    # batches of augmented image data
    train_generator = train_datagen.flow_from_directory(
        srcImagesDir + "/" + train_data_dir + "/",  # this is the target directory
        target_size=(224, 224),  # all images will be resized to 299x299
        batch_size=batchSize,
        class_mode='categorical')  # since we use categorical_crossentropy loss, we need categorical labels
    # this is a similar generator, for validation data
    validation_generator = test_datagen.flow_from_directory(
        srcImagesDir + "/" + val_data_dir + "/",
        target_size=(224, 224),
        batch_size=batchSize,
        class_mode='categorical')
    return classes, train_generator, validation_generator