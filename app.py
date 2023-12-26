from dotenv import load_dotenv

load_dotenv()  # load all the variable in persent in .env file

import streamlit as st 
import os 
import google.generativeai as genai 


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini pro model and get response 
model = genai.GenerativeModel('gemini-pro')
def get_gemini_resopnse(question):
    response = model.generate_content(question)
    return (response.text)


# initalize our strealit app 

st.set_page_config(page_title='Q&A Demo')
st.header('Gemini LLM Application')
input = st.text_input('Input',key='input')
#submit button 
submit = st.button("Ask the question")

# when click the submit button then 

if submit:
    response = get_gemini_resopnse(input)
    st.subheader('Response is :')
    st.write(response)
    

    