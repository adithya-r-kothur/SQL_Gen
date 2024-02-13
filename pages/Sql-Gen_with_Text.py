import streamlit as st
import pathlib
import textwrap
from PIL import Image
import numpy as np
import google.generativeai as genai

def ui_spacer(n=2, line=False, next_n=0):
	for _ in range(n):
		st.write('')
	if line:
		st.tabs([' '])
	for _ in range(next_n):
		st.write('')

def ui_info():
	st.markdown(f"""
	# SQL_Gen
	
	SQL query generator using Gemini-Pro API.
	""")
	ui_spacer(1)
	st.write("Made by [Adithya R Kothur](https://www.linkedin.com/in/adithya-r-kothur/).", unsafe_allow_html=True)
	ui_spacer(1)
	st.markdown("""
		Thank you for your interest in my application.
		Please be aware that this is only a Proof of Concept system
		and may contain bugs or unfinished features.
		If you like this app you can ❤️ [follow me](https://www.linkedin.com/in/adithya-r-kothur/)
		on Linkedin for news and updates.
		""")
	ui_spacer(1)
	st.markdown('Source code can be found [here](https://github.com/adithya-r-kothur).')
 
st.set_page_config(page_title ="SQL_Gen", page_icon = "📊", initial_sidebar_state = "auto") 
 
with st.sidebar:
    
    st.sidebar.success("Select a page above.")
    ui_info()

    with st.expander("Advanced"):
        st.markdown("""
        * Temperature:
        * Token length:
        """) 

    with st.expander("Tech used"):
        st.markdown("""
        * Streamlit 
        * Google Gemini-Pro API
        """)  
        
st.title("SQL_Gen")




genai.configure(api_key="AIzaSyD0oWke6DY6zHgq6jOw_CtG2aTqK8pAQcA")

model_text = genai.GenerativeModel('gemini-pro')
model_vis = genai.GenerativeModel('gemini-pro-vision')





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

