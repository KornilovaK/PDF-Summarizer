from operator import index
import streamlit as st
import plotly.express as px
import os 
from pdf import Reader

import logging
logging.basicConfig(level=logging.INFO)


with open('summary.txt', 'wb') as f:
    f = ''

with st.sidebar: 
    st.image("pdf-icon.png")
    st.title("Summarize PDF Lectures")
    choice = st.radio("Navigation", ["Welcome", "Upload and summarize pdf", "Download"])
    st.info("This project application can summarize your lecture in both English and Russian")    

if choice == "Welcome":
    st.title('Welcome Page')
    st.info("Hi. It's my little project for the dear interviewers from MTS")

if choice == "Upload and summarize pdf":
    st.title("Upload Your PDF file")
    lang = 'Russian'
    langs = ['Russian', 'English']
    lang = st.selectbox('Choose the Language', langs)

    file = st.file_uploader("PDF lecture")
    if file:
        if file.name[-3:] != 'pdf':
            st.info('Only pdf')
        else:
            if st.button('Start Summarization'): 
                with open('file.pdf', mode='wb') as w:
                    w.write(file.getvalue())

                st.info("Please, wait a little bit :)")

                reader = Reader('file.pdf')
                summary, links = reader.convert(lang)
                
                with open('summary.txt', 'wb') as f:
                    f = summary


if choice == "Download": 
    with open('summary.txt', 'rb') as f: 
        st.download_button('Download Summary', f, file_name="summary.txt")