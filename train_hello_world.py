# Learner: James Caple
# Based on tutorial at: https://developers.google.com/codelabs/tensorflow-1-helloworld#0
# 7/24/2021
#
# Simple 'Hello World' Machine Learning example using TensorFlow numpy and python.
# This example simply generates a model to fit the data provided in xs and ys.
# The model is then persisted to disk in order to demonstrate how trained models
# can 'survive' and be used without having to train it every time.
# See 'use_hello_world.py'

import tensorflow as tf
import numpy as np
from tensorflow import keras

print(tf.version.VERSION)

# Next, create the simplest possible neural network. It has one layer, that layer has one neuron, and the input shape to it is only one value.
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Train the network
model.fit(xs, ys, epochs=500)

# Use the model to predict the value of Y when X is 10
print(model.predict([10.0]))

model.summary()

# Save the entire model as a SavedModel.
model.save('saved_model/my_model')
