import streamlit as st
from PIL import Image, ImageOps
import numpy as np
from run import predict_image
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("SRCNN")
st.header("High Resolution Image at a click")
st.text("Upload your image and convert!!")
uploaded_file = st.file_uploader("Choose a low-res img ...")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=False)
    st.write("")
    st.write("Improving Quality..")
    image=image.convert('RGB')
    image=np.array(image)
    image = image[:, :, ::-1].copy() 
    image = predict_image(image)
    st.image(image,caption="High Resolution Image")
else:
    st.write("Did you upload yet? If yes, the file wasn't detectable , try again.")