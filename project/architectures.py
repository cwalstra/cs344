'''
Created on 22 sty 2018
3D Object Representations for Fine-Grained Categorization
Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei
4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.
@author: mgdak
Additions: cwalstra
'''

'''
This file implements the functions that dictate the shape of the network being trained.
'''

from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.models import Model, Sequential
from keras.applications.inception_v3 import InceptionV3
from keras.applications.vgg19 import VGG19
from keras.applications.vgg16 import VGG16
from keras import regularizers
from keras.layers.core import Flatten
from keras.layers.normalization import BatchNormalization

train_data_dir = 'cars_train'
val_data_dir = 'cars_val'
nb_train_samples = 1043
nb_val_samples = 300

def getVGG16Architecture(classes, dropoutRate):
    # create the base pre-trained model
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    for layer in enumerate(base_model.layers):
        layer[1].trainable = False

    # flatten the results from conv block
    x = Flatten()(base_model.output)

    # add another fully connected layers with batch norm and dropout
    x = Dense(4096, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(dropoutRate)(x)

    # add another fully connected layers with batch norm and dropout
    x = Dense(4096, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(dropoutRate)(x)

    # add logistic layer with all car classes
    predictions = Dense(20, activation='softmax', kernel_initializer='random_uniform',
                        bias_initializer='random_uniform', bias_regularizer=regularizers.l2(0.01), name='predictions')(
        x)

    # this is the model we will train
    model = Model(inputs=base_model.input, outputs=predictions)

    return model


def getVGG19Architecture(classes, dropoutRate):
    # create the base pre-trained model
    base_model = VGG19(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    for layer in enumerate(base_model.layers):
        layer[1].trainable = False

    # flatten the results from conv block
    x = Flatten()(base_model.output)

    # add another fully connected layers with batch norm and dropout
    x = Dense(4096, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(dropoutRate)(x)

    # add another fully connected layers with batch norm and dropout
    x = Dense(4096, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(dropoutRate)(x)

    # add logistic layer with all car classes
    predictions = Dense(20, activation='softmax', kernel_initializer='random_uniform',
                        bias_initializer='random_uniform', bias_regularizer=regularizers.l2(0.01), name='predictions')(
        x)

    # this is the model we will train
    model = Model(inputs=base_model.input, outputs=predictions)

    return model


def getInceptionV3Architecture(classes, dropoutRate):
    # create the base pre-trained model
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # InceptionV3
    x = base_model.output
    x = GlobalAveragePooling2D()(x)

    # let's add a fully-connected layer
    x = Dense(1024, activation='relu', kernel_initializer='random_uniform', bias_initializer='random_uniform',
              bias_regularizer=regularizers.l2(0.01))(x)

    # add Dropout regularizer
    x = Dropout(dropoutRate)(x)

    # and a logistic layer with all car classes
    predictions = Dense(20, activation='softmax', kernel_initializer='random_uniform',
                        bias_initializer='random_uniform', bias_regularizer=regularizers.l2(0.01), name='predictions')(
        x)

    # this is the model we will train
    model = Model(inputs=base_model.input, outputs=predictions)

    for layer in enumerate(base_model.layers):
        layer[1].trainable = False

    return model

def getMyCNN(classes, dropoutRate):
    model = Sequential()

    model.add(Conv2D(64, 3, activation='relu', input_shape=(224, 224, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, 3, activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(256, 3, activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())

    model.add(Dense(256, activation='relu', kernel_initializer='random_uniform', bias_initializer='random_uniform',
                    bias_regularizer=regularizers.l2(0.01)))

    model.add(Dense(20, activation='softmax', kernel_initializer='random_uniform',
                        bias_initializer='random_uniform', bias_regularizer=regularizers.l2(0.01), name='predictions'))

    return model