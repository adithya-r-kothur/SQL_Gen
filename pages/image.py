import streamlit as st
import pathlib
import textwrap
from PIL import Image
import numpy as np
import google.generativeai as genai

st.write("image page")

def image():
        img_file_buffer = st.camera_input("Take picture of Schema Diagram")
        if img_file_buffer is not None:
            img = Image.open(img_file_buffer)   
            response = model_vis.generate_content(['''explain what is this and write a small 
                                                   description about it ''',img])
            st.write("The summary of the Schema is:")
            st.write(response.text)
            return response.text    

genai.configure(api_key="AIzaSyD0oWke6DY6zHgq6jOw_CtG2aTqK8pAQcA")

model_text = genai.GenerativeModel('gemini-pro')
model_vis = genai.GenerativeModel('gemini-pro-vision')

def genai_img():
    st.write("Upload a Schema Diagram of the tables and give the prompt to generate SQL queries.")
    text_from_image  = image()  
        
    if(text_from_image is None):
        st.write("Please take a pic of schema diagram to generate")
    else:
        sql_query = st.text_input('Enter the conditons for the sql query')
        img_prompt ='''Hello Adithya'''
        if(len(text_from_image)>0):
            response = model_text.generate_content(img_prompt+text_from_image + sql_query)
        
        st.write("The SQL query is:")
        if len(sql_query) > 0:
            st.write(response.text)
            
            
            
genai_img()            
            
            
            