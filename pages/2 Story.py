import streamlit as st
from PIL import Image

st.markdown("""<style>
            .css-10trblm.e16nr0p30{
                    color: cadetblue;}

            </style>""", unsafe_allow_html=True)

logo = Image.open('../get_it_right_frontend/assets/story.png')
st.image(logo,width=600, use_column_width=None, )

st.title("Story time")
st.write("Catch trash, code it to give it a second life")
st.write("This is the story of how a your waste can be valued and given a second life")
