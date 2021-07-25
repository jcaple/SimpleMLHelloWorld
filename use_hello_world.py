# Learner: James Caple
# Based on tutorial at: https://developers.google.com/codelabs/tensorflow-1-helloworld#0
# 7/24/2021
#
# Simple 'Hello World' Machine Learning example using TensorFlow numpy and python.
# This example shows how to use the model generated by the 'train_hello_world.py'
# script.

import tensorflow as tf
import numpy as np
from tensorflow import keras

print(tf.version.VERSION)

new_model = tf.keras.models.load_model('saved_model/my_model')

# Check its architecture
new_model.summary()

# Use the model to predict the value of Y when X is 10.  Should be close to 31.
print(new_model.predict([10.0]))

# Use the model to predict the value of Y when X is 96.  Should be close to 289.
print(new_model.predict([96.0]))