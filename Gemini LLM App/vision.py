import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key= "YOUR_GOOGLE_API_KEY")

## function to load Gemini Vision Pro Model and get responses
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(image, input):
    if input != "":
        response = model.generate_content([image, input])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

input = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

if submit:
    response = get_gemini_response(image, input)
    st.subheader("The Response is")
    st.write(response)