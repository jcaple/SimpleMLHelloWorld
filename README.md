# A Simple 'Hello World' Machine Learning (ML) Example In Python

## Description

This is a simple project demonstrating the most basic ML example I could find on the
internet:

https://developers.google.com/codelabs/tensorflow-1-helloworld#0

There were three or four questions I wanted to answer with this example:

1.  What is the simples ML example of training a model I could write?
1.  Give me a simple example using TensorFlow so I can start to get familiar with it.
1.  When the model is created, where does it 'live' and how might I re-use it
without having to train it every time.
1.  Given a simple ML example, how does it's computation compare to a programmed
version of the same?  This is one key question I have about ML models, especially
with regard to chess, for example.  How do trained chess ML models compare with the
hand-crafted chess game engines?  Are they better, worse, faster, slower?  This example
is too simple to provide an answer, but the comparison is interesting, I think.

## To Train The Brain/Model

First, you'll need to install TensorFlow and Numpy:

1.  `pip install --upgrade pip`
1.  `pip install tensorflow`
1.  `pipe install numpy`
1.  Then run the training example:
    `python3 train_hello_world.py`
1.  To re-use the model you just generated, run:
    `python3 use_hello_world.py`
1.  Finally, to run a simple function to calculate the same results, run:
    `python3 simple_func.py`