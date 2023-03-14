import streamlit as st
import numpy as np
import pickle

'''
#Loading the model
Loaded_model_B&NB = pickle.load(open('D:/Work/Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))
Loaded_model_types = pickle.load(open('D:/Work/Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))
input_data = Uploaded_Image

# creating a function for Prediction

def class_prediction(input_data):
    prediction = Loaded_model_B&NB.predict(input_data)
    print(prediction)

    if (prediction[0] == B):
      return 'Biodegradable'
    elif(prediction[0] == NB):
        print('Non_Biodegradable')
        prediction = Loaded_model_types.predict(input_data)
        return prediction
    else:
        return 'Trash'
'''

def main():

    # giving a title
    st.title('Get It Right')
    st.write("Upload an image and i will tell you what type of waste is it")
    # getting the input data from the user

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
    # You can access the file contents using .read()
        image = uploaded_image.read()
        st.image(image, caption='Uploaded Image.', use_column_width=True)

    # code for Prediction
    classification = 'test'

    # creating a button for Prediction

    #if st.button('Trash Classification'):
        #classification = class_prediction([user_image])

    st.success(classification)

if __name__ == '__main__': #check if this line is needed !
    main()
