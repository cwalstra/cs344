'''
This file examines the properties of the Boston Housing Price dataset supplied by Keras

Written by: Chris Walstra, based on code supplied by Keith Vander Linden
'''

import numpy as np
from keras.datasets import boston_housing
from keras.utils import to_categorical


def print_structures():
    print(
        f'training images \
            \n\tcount: {len(train_images)} \
            \n\tdimensions: {train_images.ndim} \
            \n\tshape: {train_images.shape} \
            \n\tdata type: {train_images.dtype}\n\n',
        f'testing images \
            \n\tcount: {len(test_labels)} \
            \n\tdimensions: {train_labels.ndim} \
            \n\tshape: {test_labels.shape} \
            \n\tdata type: {test_labels.dtype} \
            \n\tvalues: {test_labels}\n',
    )

(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

print_structures()