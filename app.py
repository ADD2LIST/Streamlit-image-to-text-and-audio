import streamlit as st
from PIL import Image
import pytesseract
import pyttsx3
from googletrans import Translator

# Function to convert image to text and speech
def convert_image_to_speech(image):
    # Open the image
    img = Image.open(image)

    # Perform OCR on the image
    result = pytesseract.image_to_string(img)

    # Translate the text to German
    translator = Translator()
    translated_text = translator.translate(result, dest='german').text

    # Initialize pyttsx3 engine for speech synthesis
    engine = pyttsx3.init()

    # Convert the translated text to speech
    engine.say(translated_text)
    engine.runAndWait()

    # Return the extracted text and translated text
    return result, translated_text

# Streamlit application
def main():
    st.title("Image to Text and Speech Conversion")
    st.write("Upload an image and convert it to text and speech")

    # File upload
    uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Convert image to text and speech
        if st.button('Convert'):
            extracted_text, translated_text = convert_image_to_speech(uploaded_file)

            # Display the extracted text and translated text
            st.subheader("Extracted Text:")
            st.write(extracted_text)

            st.subheader("Translated Text (German):")
            st.write(translated_text)

if __name__ == '__main__':
    main()
    
