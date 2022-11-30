import numpy as np
from keras.models import Model
from keras.layers import Dense, Activation, Lambda, Input, Concatenate, Multiply
from keras.metrics import binary_accuracy
from keras.losses import binary_crossentropy
import keras.backend as K

