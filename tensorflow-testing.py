from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas
import os
import numpy as np
import pathlib
import IPython.display as display
import matplotlib.pyplot as plt
from PIL import Image

import tensorflow as tf

data_directory = pathlib.WindowsPath("./images")
classes = np.array([item.name for item in data_directory.glob(
    '*') if item.name != "LICENSE.txt"])


image_generator = ImageDataGenerator(rescale=1./255)

dataset = image_generator.flow_from_directory(directory=str(data_directory),
                                              batch_size=32,
                                              shuffle=True,
                                              target_size=(300, 500),
                                              classes=list(classes))


image_batch, label_batch = next(dataset)

print(label_batch)

dataset.flow_from_directory()