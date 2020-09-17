import streamlit as st
from PIL import Image

im=Image.open('Logo.png')
st.image(im,use_column_width=True)

st.write("OK")
