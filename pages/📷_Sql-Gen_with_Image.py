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
    
    with st.expander("About"):
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


def image():
        img_file_buffer = st.camera_input("Take picture of Schema Diagram")
        if img_file_buffer is not None:
            img = Image.open(img_file_buffer)   
            response = model_vis.generate_content(['''Given an image of a SQL database schema, analyze and extract relevant details such as tables, columns, relationships, 
                and any notable constraints or keys present in the schema. Provide a comprehensive understanding of the structure 
                depicted in the image.
                ''',img])
            st.write("The summary of the Schema is:")
            st.write(response.text)
            return response.text  
        
def upload():
    uplaod_img = st.file_uploader("Upload a Schema Diagram of the tables if you did'nt click a pic", type=["jpg", "png", "jpeg"])
    if uplaod_img is not None:
        img_x = Image.open(uplaod_img)
        responce = model_vis.generate_content(['''Given an image of a SQL database schema, analyze and extract relevant details such as tables, columns, relationships, 
            and any notable constraints or keys present in the schema. Provide a comprehensive understanding of the structure 
            depicted in the image.
            ''',img_x])
        st.write("The summary of the Schema is:")
        st.write(responce.text)
        return responce.text
              

genai.configure(api_key="AIzaSyD0oWke6DY6zHgq6jOw_CtG2aTqK8pAQcA")

model_text = genai.GenerativeModel('gemini-pro')
model_vis = genai.GenerativeModel('gemini-pro-vision')

def genai_img():
    
    st.write("Upload a Schema Diagram of the tables and give the prompt to generate SQL queries.")
    text_from_image  = image() 
    text_from_uploadd = upload()
    
        
    if(text_from_image is None):
        st.write("Please take a pic or upload the schema diagram to generate")
        if(text_from_uploadd is not None):
            text_from_image = text_from_uploadd
            sql_query = st.text_input('Enter the conditons for the sql query')
            img_prompt ='''Hello Adithya'''
            if(len(text_from_image)>0):
                response = model_text.generate_content(img_prompt+text_from_image + sql_query)
        
            st.write("The SQL query is:")
            if len(sql_query) > 0:
                st.write(response.text)
            
    else:
        sql_query = st.text_input('Enter the conditons for the sql query')
        img_prompt ='''given the details of sql schema and conditions for the query 
            Generate an optimal SQL query that effectively retrieves the desired data.
            Ensure the resulting query adheres to standard SQL syntax and is well-suited to the structure identified in the 
            image along with the specified conditions.
            '''
        if(len(text_from_image)>0):
            response = model_text.generate_content(img_prompt+text_from_image + sql_query)
        
        st.write("The SQL query is:")
        if len(sql_query) > 0:
            st.write(response.text)
            
            
            
genai_img()            
            
            
            