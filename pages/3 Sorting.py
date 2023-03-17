import streamlit as st
import numpy as np


    # giving a title
st.title('Sort your bin here!')
st.write("Upload an image and i will tell you what type of waste is it")

    # getting the input data from the user

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], )

if uploaded_image is not None:
    # You can access the file contents using .read()
    image = uploaded_image.read()
    st.image(image, caption='Uploaded Image.', use_column_width=True, )

    # code for Prediction
classification = 'test'

    # creating a button for Prediction

#if st.button('Trash Classification'):
    #classification = class_prediction([uploaded_image])

st.success(classification)



# Create radio buttons to select the page
#selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page with its function
#pages[selection]()
