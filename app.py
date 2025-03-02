from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API-KEY"))

# function to generate response
model=genai.GenerativeModel("models/gemini-2.0-flash")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Simple CHATGPT Application")

input=st.text_input("Input: ",key="input")
submit=st.button("ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)