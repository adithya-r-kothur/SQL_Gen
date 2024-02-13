import streamlit as st
import pathlib
import textwrap
from PIL import Image
import numpy as np
import google.generativeai as genai




genai.configure(api_key="AIzaSyD0oWke6DY6zHgq6jOw_CtG2aTqK8pAQcA")

model_text = genai.GenerativeModel('gemini-pro')
model_vis = genai.GenerativeModel('gemini-pro-vision')


st.write("text page")


def genai_text():
    st.write("Please enter the written details of the sql schema with all the details")
    
    schema_details = st.text_input("Enter the details of the schema") 
    
    text_prompt ='''Hello Adithya'''
    
    query = st.text_input('Enter the conditons of the sql query')    
    if(len(schema_details)>0  and len(query)>0):
        response = model_text.generate_content(text_prompt+schema_details+query)
        
        st.write("The SQL query is:")
        st.write(response.text)   


genai_text()

