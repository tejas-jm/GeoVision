import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Location Image Classifier")
st.text("Provide URL of Location Image for image classification")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('models/Image_Location_Generator.h5')  # Load your model
    return model

@st.cache_data
def initialize_location_classifier():
    # Code for initializing your location image classifier
    classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
    return classes

model = load_model()
classes = initialize_location_classifier()

def decode_img(image):
    try:
        img = tf.image.decode_jpeg(image, channels=3)
        img = tf.image.resize(img, [150, 150])
        return np.expand_dims(img, axis=0)
    except tf.errors.InvalidArgumentError as e:
        st.error("Invalid image format. Please provide a valid JPEG, PNG, GIF, or BMP image.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while decoding the image: {str(e)}")
        st.stop()

path = st.text_input('Enter Image URL to Classify.. ',
                     'https://storage.googleapis.com/image_classification_2021/Glacier-Argentina-South-America-blue-ice.JPEG')

if path is not None:
    content = requests.get(path).content
    st.write("Predicted Class:")
    with st.spinner('classifying.....'):
        label = np.argmax(model.predict(decode_img(content)), axis=1)
        st.write(classes[label[0]])
    st.write("")
    image = Image.open(BytesIO(content))
    st.image(image, caption='Classifying Image', use_column_width=True)
