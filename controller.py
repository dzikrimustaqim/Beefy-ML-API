from fastapi import UploadFile

import tensorflow as tf
from keras.utils import load_img, img_to_array
import numpy as np
from PIL import Image

def preprocessing(fileImage: UploadFile):
    img = Image.open(fileImage.file).resize((224, 224))
    img_array = img_to_array(img)
    img_preprocessed = tf.keras.applications.resnet50.preprocess_input(np.expand_dims(img_array, axis=0))
    return img_preprocessed

def post_preprocessing(img_postpreprocessing):
    model = tf.keras.models.load_model('./models/softmax_new_model.h5')
    predictions = model.predict(img_postpreprocessing)
    predicted_class = np.argmax(predictions, axis=1)[0]
    class_labels = ['fresh', 'spoiled']
    predicted_label = class_labels[predicted_class]
    predicted_probability = predictions[0][predicted_class] * 100
    return predicted_label, predicted_probability


def predictMeat(file: UploadFile):
    try:
        image = preprocessing(fileImage=file)
        label, probability = post_preprocessing(img_postpreprocessing=image)
        response = {
            'label': label,
            'pobability': probability
        }
        return (True, response)
    except:
        return (False, None)