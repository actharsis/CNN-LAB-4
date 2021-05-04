import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import glob
import pathlib
from datetime import datetime
import random

data_dir = pathlib.Path('/home/administrator/food-101')

logdir = "logs/" + datetime.now().strftime("%Y%m%d-%H%M%S")

file_writer = tf.summary.create_file_writer(logdir)
    
all_images = list(data_dir.glob('*/*'))
images = []
for i in range(0, 6):
	a = PIL.Image.open(str(random.choice(all_images)))

	a = a.resize((300, 300), PIL.Image.ANTIALIAS)

	pix = np.array(a)

	img = np.reshape(pix, (300, 300, 3))
	images.append(img)

ar = np.array(images)

#ar = tf.keras.layers.experimental.preprocessing.RandomRotation(factor=0.04, fill_mode='constant')(ar)
#ar = tf.keras.layers.experimental.preprocessing.RandomCrop(120, 120)(ar)
ar = tf.keras.layers.experimental.preprocessing.RandomFlip(mode="vertical")(ar)

with file_writer.as_default():
  	tf.summary.image("Training data", ar, step=1, max_outputs=15)
