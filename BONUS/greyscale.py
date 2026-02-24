import streamlit as st
from PIL import Image
 
st.subheader("Color to Grayscale Converter")

st.write("Upload an image to convert it to grayscale.")
uploaded_file = st.file_uploader("Choose an image")
 
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
 
if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

if uploaded_file:
    image = Image.open(uploaded_file)
    grey_uploaded_file = image.convert("L")
    st.image(grey_uploaded_file)