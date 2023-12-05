# Common imports
from tqdm import tqdm
from glob import glob
import numpy as np
import imghdr

# Data imports
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.image import resize

# Model imports
from keras.models import load_model

# CSV file imports
from datetime import datetime
import csv
import os

# Categories
class_names = {0: 'cloudy', 1: 'foggy', 2: 'rainy', 3: 'shine', 4: 'sunrise'}

def load_image(path):
    '''
    Takes in path of the image and load it
    '''
    return resize(img_to_array(load_img(path)) / 255., (256, 256))

def load_data(img_paths):
    '''
    Takes in path of the images and loads all
    '''
    X = np.zeros(shape=(len(img_paths), 256, 256, 3))
    for i, path in tqdm(enumerate(img_paths), desc='Loading'): X[i] = load_image(path)
    return X


# Load images
image_paths = [
    x for x in sorted(glob('./data/*.jpg'))
    if imghdr.what(x) is not None or print(f'error: file {x} is not a valid image')
]
print(f'number of valid images: {len(image_paths)}')

# Check the existing processed files
output_dir = './result/'
# Extract processed image names from existing CSV files
processed_images = set()
for result_file in glob(os.path.join(output_dir, 'predictions_*.csv')):
    with open(result_file, 'r') as f:
        for row in csv.reader(f):
            processed_images.add(row[0])

# Filter already processed images
unprocessed_image_paths = [path for path in image_paths if os.path.basename(path) not in processed_images]
print(f'number of unprocessed images: {len(unprocessed_image_paths)}')

# Ask user if they want to skip processing already predicted images
processed_to_write = image_paths if input('processing already predicted images? (Y/n): ') or 'Y' == 'Y' else unprocessed_image_paths
if len(processed_to_write) == 0:
    print('no images to process')
    exit()

# Load model
model_v3 = load_model('./data/ResNet152V2-Weather-Classification-03.h5')

# Make Predictions
preds = np.argmax(model_v3.predict(load_data(processed_to_write)), axis=-1)

# Get timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generate CSV file name based on timestamp
csv_file_path = f'{output_dir}predictions_{timestamp}.csv'

# Write predictions to the CSV file
with open(csv_file_path, mode='w', newline='') as file:  # 'a' mode for appending to an existing file
    writer = csv.writer(file)
    for i, image_path in enumerate(processed_to_write):
        writer.writerow([os.path.basename(image_path), class_names[preds[i]]])

print('csv file successfully generated')
