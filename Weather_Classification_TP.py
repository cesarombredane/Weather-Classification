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

# Categories
class_names = {0: 'cloudy', 1: 'foggy', 2: 'rainy', 3: 'shine', 4: 'sunrise'}


def load_image(path):
    '''
    Takes in path of the image and load it
    '''
    img = resize(img_to_array(load_img(path)) / 255., (256, 256))
    return img


def load_data(img_paths):
    '''
    Takes in path of the images and loads all
    '''
    X = np.zeros(shape=(len(img_paths), 256, 256, 3))
    for i, path in tqdm(enumerate(img_paths), desc="Loading"):
        X[i] = load_image(path)

    return X


# Load images
image_paths = sorted(glob('./data/*.jpg'))
print(f"Total Number of Images: {len(image_paths)}")

# Check the existing processed files
output_dir = './result/'
existing_result_files = glob(os.path.join(output_dir, 'predictions_*.csv'))
# Extract processed image names from existing CSV files
processed_images = set()
for result_file in existing_result_files:
    with open(result_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            image_name = row[0]
            processed_images.add(image_name)

# Filter already processed images
unprocessed_image_paths = [path for path in image_paths if os.path.basename(path) not in processed_images]
print(f"Total Number of Unprocessed Images: {len(unprocessed_image_paths)}")

if len(unprocessed_image_paths) == 0:
    print("All images have been processed! The CSV sum-up is/are already in the result folder.")
    exit()
elif len(unprocessed_image_paths) == len(image_paths):
    print("All images in the data folder are unprocessed, so the prediction of all images will now begin...")

    # Load all images for prediction
    images = load_data(image_paths)
    processed_to_write = image_paths
else:
    # Interactive prompt for user choice
    skip_processed = input("Do you want to skip processing already predicted images? (yes/no): ").lower()

    if skip_processed == 'yes':
        # Load unprocessed images for prediction
        images = load_data(unprocessed_image_paths)
        processed_to_write = unprocessed_image_paths
    else:
        # Load all images for prediction (processed and unprocessed)
        images = load_data(image_paths)
        processed_to_write = image_paths

# Load model
model_v3 = load_model('./data/ResNet152V2-Weather-Classification-03.h5')

# Make Predictions
preds = np.argmax(model_v3.predict(images), axis=-1)

# Get timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Generate CSV file name based on timestamp
csv_file_path = f'{output_dir}predictions_{timestamp}.csv'

# Write predictions to the CSV file
with open(csv_file_path, mode='w', newline='') as file:  # 'a' mode for appending to an existing file
    writer = csv.writer(file)
    for i, image_path in enumerate(processed_to_write):
        image_name = os.path.basename(image_path)
        prediction_label = class_names[preds[i]]
        writer.writerow([image_name, prediction_label])

print("New CSV file based on your choice has been successfully generated!")
