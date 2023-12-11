from fastapi import FastAPI, File, UploadFile
from keras.models import load_model
from tensorflow.keras.utils import img_to_array
from tensorflow.image import resize
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()

# Charger le modèle (Assurez-vous que le chemin est correct)
model = load_model('./data/ResNet152V2-Weather-Classification-03.h5')

# Catégories
class_names = {0: 'cloudy', 1: 'foggy', 2: 'rainy', 3: 'shine', 4: 'sunrise'}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Convertir l'image reçue en un array numpy
    contents = await file.read()
    pil_image = Image.open(BytesIO(contents))
    image_array = img_to_array(pil_image)

    # Prétraiter l'image
    image = resize(image_array / 255., (256, 256))
    image = np.expand_dims(image, axis=0)  # Ajouter une dimension pour le batch

    # Faire la prédiction
    prediction = model.predict(image)
    predicted_class = class_names[np.argmax(prediction, axis=-1)[0]]
    
    return {"filename": file.filename, "prediction": predicted_class}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
