import streamlit as st
import numpy as np
import requests
from PIL import Image
import io

# giving a title
st.title('Sort your bin here!')
st.write("Upload an image and i will tell you what type of waste is it")

# getting the input data from the user
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], )

if uploaded_image is not None:
    image = uploaded_image.getvalue()
    # image = Image.open(io.BytesIO(uploaded_image.read()))
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    # You can access the file contents using .read()
    st.write("Classifying...")
    response = requests.post("https://get-it-right-2fv75ren5q-ew.a.run.app/upload_image",files={"file": image})
    response_predict = requests.get("https://get-it-right-2fv75ren5q-ew.a.run.app/predict_one")
    st.write(response_predict.text)


#pages[selection]()
