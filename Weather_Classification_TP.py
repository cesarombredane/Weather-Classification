#!/usr/bin/env python
# coding: utf-8
# Taken from : https://www.kaggle.com/datasets/utkarshsaxenadn/weather-classification-resnet152v2

# Common
from tqdm import tqdm
from glob import glob
import pandas as pd
import numpy as np
import keras

# Data
from sklearn.model_selection import StratifiedShuffleSplit
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.image import resize

# Data Viz
import matplotlib.pyplot as plt
import seaborn as sns

# TL Model
from tensorflow.keras.applications import ResNet50, ResNet50V2, InceptionV3, Xception, ResNet152, ResNet152V2

# Model
from keras.layers import Dense, GlobalAvgPool2D, Dropout
from keras.models import load_model
from keras import Sequential

# Callbacks 
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Model Performance
from sklearn.metrics import classification_report

# Model Viz
from tensorflow.keras.utils import plot_model

# CSV file
from datetime import datetime
import csv
import os


# Cateories
class_names = {0: 'cloudy', 1: 'foggy', 2: 'rainy', 3: 'shine', 4: 'sunrise'}

def load_image(path):
    '''
    Takes in path of the image and load it
    '''
    img = resize(img_to_array(load_img(path))/255., (256,256))
    return img

# def show_image(image, title=None):
#     '''
#     Takes in an Image and plot it with Matplotlib
#     '''
#     plt.imshow(image)
#     plt.title(title)
#     plt.axis('off')

def load_data(img_paths):
    X = np.zeros(shape=(len(img_paths), 256,256,3))
    for i, path in tqdm(enumerate(img_paths), desc="Loading"):
        X[i] = load_image(path)
    
    return X

# Load images
image_paths = sorted(glob('./data/*.jpg'))
print(f"Total Number of Images : {len(image_paths)}")
image_paths[:5]
images = load_data(image_paths)

# Data Viz
# plt.figure(figsize=(10,10))
# for i in range(25):
    
#     if i > len(images)-1:
#         break
    
#     image = images[i]

#     plt.subplot(5,5,i+1)
#     show_image(image, title=f"Image : {i}")
# plt.tight_layout()
# plt.show()

# Prediction with pre-trained ResNet152V2 model
# Load model
model_v3 = load_model('./data/ResNet152V2-Weather-Classification-03.h5')

# Result
# print("image showing part start")
# plt.figure(figsize=(15,20))
# for i, im in enumerate(images):

#     # Make Prediction
#     pred = class_names[list(preds)[i]]
    
#     # Show Prediction
#     plt.subplot(5,5,i+1)
#     show_image(im, title=f"Pred : {pred}")

# plt.tight_layout()
# plt.show()
# print("image showing part done")

output_dir = './result/'
pre_computed = {}
for i, result_file in enumerate(output_dir):
    result_path = os.path.basename(result_file)
    if not result_path.endswith('.csv'): continue
    with open(result_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] not in pre_computed: pre_computed[row[0]] = row[1]

# TODO: use precomputed 
# Make Predictions
preds = np.argmax(model_v3.predict(images), axis=-1)

# Generate CSV file
# Generating timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_file_path = f'{output_dir}predictions_{timestamp}.csv'

# Writing predictions to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image_name', 'prediction_label'])
    for i, image_path in enumerate(image_paths):
        image_name = os.path.basename(image_path)
        prediction_label = class_names[preds[i]]
        writer.writerow([image_name, prediction_label])

print("CSV file generated at: " + csv_file_path)
