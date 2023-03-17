import streamlit as st
from PIL import Image


st.markdown("""<style>
            .css-10trblm.e16nr0p30{
                    color: cadetblue;}

            </style>""", unsafe_allow_html=True)
#logo reading

logo = Image.open('../get_it_right_frontend/assets/team.png')
st.image(logo,width=600, use_column_width=None, )
st.title("Team")
st.write("We are the trash dealers")
