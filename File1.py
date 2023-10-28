import streamlit as st
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an GestureRecognizer object.
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

st.title("Test")
st.header("Test")

picture=st.camera_input("Test")

if picture:
  with open('gesture.jpg', 'wb') as f:
    f.write(picture.read())
  
  # STEP 3: Load the input image.
  image = mp.Image.create_from_file('gesture.jpg')

  # STEP 4: Recognize gestures in the input image.
  recognition_result = recognizer.recognize(image)

st.write(recognition_result)
