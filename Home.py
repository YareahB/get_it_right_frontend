import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

#styling
# def get_style():
#     with open("style.css") as f:
#         st.markdown("""<link rel="stylesheet" type="text/css" href="style.css">""", unsafe_allow_html=True)
# get_style()


st.markdown("""<style>
            .css-10trblm.e16nr0p30{
                    color: cadetblue;}

            </style>""", unsafe_allow_html=True)

#logo reading
logo = Image.open('../get_it_right_frontend/assets/home.png')
st.image(logo,width=700, use_column_width=None, )

def main():
    st.title("Home Page")
    st.write("Welcome on board!")

if __name__ == '__main__':
    main()
