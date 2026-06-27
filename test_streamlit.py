import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai


# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


# Streamlit UI
st.title("Gemini Chat App 🤖")

user_input = st.text_input("Enter your message:")


if user_input:
    response = model.generate_content(user_input)

    st.write("Gemini Response:")
    st.write(response.text)