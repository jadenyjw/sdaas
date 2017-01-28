import tflearn
from tflearn.data_utils import shuffle
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
from tflearn.layers.normalization import local_response_normalization

import h5py
from tflearn.data_utils import build_hdf5_image_dataset

network = input_data(shape=[None, 66, 200, 3],
                     data_preprocessing=img_prep)
