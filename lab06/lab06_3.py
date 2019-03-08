'''
This file examines the properties of the Boston Housing Price dataset supplied by Keras

Written by: Chris Walstra, based on code supplied by Keith Vander Linden
'''

import numpy as np
from keras.datasets import boston_housing


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

print("Part I")
print(f'Number of training images: {len(train_images)}')
print(f'Number of testing images: {len(test_labels)}')

print("Part II")
print(f'Training Example rank: {train_images.ndim}')
print(f'Training Example shape: {train_images.shape}')
print(f'Training Example data type: {train_images.dtype}')

print(f'Testing Example rank: {test_labels.ndim}')
print(f'Testing Example shape: {test_labels.shape}')
print(f'Testing Example data type: {test_labels.dtype}')