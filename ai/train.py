import tflearn
from tflearn.data_utils import shuffle
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

import h5py
from tflearn.data_utils import build_hdf5_image_dataset

# Make sure the data is normalized
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()

# Create extra synthetic training data by flipping, rotating and blurring the
# images on our data set.
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=25.)
img_aug.add_random_blur(sigma_max=3.)

network = input_data(shape=[None, 66, 200, 3], data_preprocessing=img_prep)
network = conv_2d(network, nb_filter=[31, 98, 24], filter_size=[5,5], strides=[2,2], activation='relu')
network = conv_2d(network, nb_filter=[14, 47, 36], filter_size=[5,5], strides=[2,2], activation='relu')
network = conv_2d(network, nb_filter=[31, 98, 24], filter_size=[5,5], strides=[2,2], activation='relu')

network = conv_2d(network, nb_filter=[31, 98, 24], filter_size=[3,3], activation='relu')
network = conv_2d(network, nb_filter=[31, 98, 24], filter_size=[3,3], activation='relu')


network = fully_connected(network, 1164, activation='relu')
network = fully_connected(network, 100, activation='relu')
network = fully_connected(network, 50, activation='relu')
network = fully_connected(network, 10, activation='relu')
network = fully_connected(network, 1, activation='relu')

network = regression(network, optimizer='momentum',
                     loss='mean_square')

model = tflearn.DNN(network, tensorboard_verbose=0)

# Train it! We'll do 100 training passes and monitor it as it goes.
model.fit(X, Y, n_epoch=50, shuffle=True, validation_set=(X_val, Y_val),
          show_metric=True,
          snapshot_epoch=True,
          run_id='carnet')

# Save model when training is complete to a file
model.save("carnet.tfl")
