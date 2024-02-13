#imports 
import streamlit as st
import pathlib
import textwrap
from PIL import Image
import numpy as np
import google.generativeai as genai

############################################################################


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
        
st.title("**Welcome to SQL-Gen!**")

st.write('''


## Image Page:

On this page, you can generate SQL queries using visual representations of database schemas. Simply upload an image of your database schema, and let our advanced image recognition algorithms analyze and interpret it. The app will then translate the visual structure into SQL queries, making it incredibly easy for you to interact with your database.

### How to use:
1. Upload your database schema image.
2. The app will analyze and extract the essential information.
3. Review and customize the generated SQL queries as needed.
4. Execute the queries directly or save them for future use.

**Why use the Image Page?**
- Ideal for users who have a visual representation of their database structure.
- Quick and intuitive way to generate SQL queries without manual input.

## Text Description Page:

This page is designed for users who prefer describing their database structure using text. If you have a detailed textual description of your database schema, you can leverage this page to generate accurate SQL queries.

### How to use:
1. Input the text description of your database schema.
2. The app will process the information and create corresponding SQL queries.
3. Review and edit the generated queries if necessary.
4. Execute the queries directly or save them for future use.

**Why use the Text Description Page?**
- Suitable for users who prefer describing database structures through text rather than images.
- Helpful for situations where you have written documentation of your database.

---

With SQL-Gen, generating SQL queries becomes a breeze, whether you prefer a visual approach or a textual one. Feel free to explore both pages and choose the method that suits your workflow best. If you have any questions or feedback, don't hesitate to reach out through our support channels. Happy querying!''')








 
    
    

