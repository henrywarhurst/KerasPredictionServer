# Flask
from flask import Flask, request

# Keras
from keras.applications import VGG16
from keras.preprocessing.image import img_to_array, load_img

# Numpy
import numpy as np

# Misc
import os

# Init the Keras model
model = VGG16(weights='imagenet',
                  include_top=True,
                  input_shape=(224, 224, 3))

# Init the flask app
app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def get_prediction():
	if request.method == 'POST':

		file = request.files['image']
		file.save('./x.jpeg')

		img = load_img('./x.jpeg', target_size=(224, 224))
		x = img_to_array(img)
		x = x.reshape((1,) + x.shape)

		predictions = model.predict(x)
		result = np.argmax(predictions)

		os.remove('./x.jpeg')

		return str(result)
