import streamlit as st
from google.generativeai import discuss
from PIL import Image
import pytesseract
from gtts import gTTS

# Initialize the Google Gemini API
import google.generativeai as genai
genai.configure(api_key="AIzaSyCVd1D7sqroAOjKjY5c0eIzDaf8OhGyHvU")

# Streamlit configuration
st.title("AI-Powered Solution with Google Gemini API")

# File uploader
uploaded_image = st.file_uploader(r"C:\Users\91703\OneDrive\Pictures - Copy\Saved Pictures\mis.jpg", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Real-Time Scene Understanding
    st.subheader("Real-Time Scene Understanding")
    
    # Extract text from the image using OCR
    text_from_image = pytesseract.image_to_string(image)
    st.write("Extracted text (for context):", text_from_image)

    # Use Google Gemini API to generate a scene description
    prompt = f"Describe the scene from this text: {text_from_image}"
    response = genai.generate_text(prompt=prompt)
    
    # Display the response
    scene_description = response["candidates"][0]["output"]
    st.write("AI-Generated Scene Description:", scene_description)


if text_from_image.strip():
    tts = gTTS(text=text_from_image, lang="en")
    tts_output_path = "text_to_speech.mp3"
    tts.save(tts_output_path)
    st.audio(tts_output_path, format="audio/mp3")
else:
    st.warning("No text found in the image.")
