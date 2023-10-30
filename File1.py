import streamlit as st
import mediapipe as mp
import os
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# STEP 2: Create an GestureRecognizer object.
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

print(os.listdir())

st.title("Test")
st.header("Test")

picture=st.camera_input("Test")

if picture:
# Convert BGR to RGB
    picture_rgb = picture[:, :, ::-1]

    # Display the captured image
    st.image(picture_rgb, channels="BGR")

    # Process the captured image with Mediapipe
    rgb_frame = mp.Image(image_format=ImageFormat.SRGB, data=picture_rgb)

      # STEP 4: Recognize gestures in the input image.
    recognition_result = recognizer.recognize(rgb_frame)

    st.write(recognition_result)
