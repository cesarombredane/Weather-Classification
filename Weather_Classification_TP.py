# Common imports
from tqdm import tqdm
from glob import glob
import numpy as np

# Data imports
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.image import resize

# Model imports
from keras.models import load_model

# CSV file imports
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

# pre_computed = {}
# for i, result_file in enumerate(output_dir):
#     result_path = os.path.basename(result_file)
#     if not result_path.endswith('.csv'): continue
#     with open(result_file, 'r') as f:
#         reader = csv.reader(f)
#         next(reader)
#         for row in reader:
#             if row[0] not in pre_computed: pre_computed[row[0]] = row[1]

def load_data(img_paths):
    '''
    Takes in path of the images and loads all
    '''
    X = np.zeros(shape=(len(img_paths), 256,256,3))
    for i, path in tqdm(enumerate(img_paths), desc="Loading"):
        X[i] = load_image(path)
    
    return X

# Load images
image_paths = sorted(glob('./data/*.jpg'))
print(f"Total Number of Images : {len(image_paths)}")
image_paths[:5]
images = load_data(image_paths)

# Prediction with pre-trained ResNet152V2 model
# Load model
model_v3 = load_model('./data/ResNet152V2-Weather-Classification-03.h5')

# Make Predictions
preds = np.argmax(model_v3.predict(images), axis=-1)

# Generating timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Generate CSV file
output_dir = './result/'
csv_file_path = f'{output_dir}predictions_{timestamp}.csv'

# Writing predictions to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image_name', 'prediction_label'])
    for i, image_path in enumerate(image_paths):
        image_name = os.path.basename(image_path)
        prediction_label = class_names[preds[i]]
        writer.writerow([image_name, prediction_label])
