import tensorflow as tf
import numpy as np


def maximum(x1, x2):
    return tf.maximum(x1, x2)


def minimum(x1, x2):
    return tf.minimum(x1, x2)


def argsort(x, axis=-1):
    return tf.argsort(x, axis=axis)


def concatenate(tensors, axis):
    return tf.concat(tensors, axis=axis)


def cast(x, dtype):
    return tf.cast(x, dtype)


def log(x):
    return tf.math.log(x)


def abs(x):
    return tf.math.abs(x)


def exp(x):
    return tf.math.exp(x)


def argmax(x, axis):
    return tf.argmax(x, axis=axis)


def squeeze(x, axis):
    return tf.squeeze(x, axis)


def zeros(shape):
    return tf.zeros(shape)


def square(x):
    return tf.square(x)


def expand_dims(x, axis):
    return tf.expand_dims(x, axis)


def zeros_like()
