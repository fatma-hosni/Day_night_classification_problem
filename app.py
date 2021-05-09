
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
import cv2

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


def model_predict(img_path, model):
    
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(600,600))
    img = np.reshape(img,[1,600,600,3])
    img=img/255.0
    print(img_path)
    prediction = model.predict(img)

    return prediction

app = Flask(__name__)


# Load your trained model
loaded_model = tf.keras.models.load_model(r'saved_model/my_model')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, loaded_model)

        cls_name=""
        if preds[0]<0.5:
            cls_name=("its a day")
        else:
            cls_name=("its a night")
        return cls_name
    return None


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)


