import streamlit as st
import os 
from pdf import Reader


with st.sidebar: 
    st.image("pdf-icon.png")
    st.title("Summarize PDF Lectures")
    choice = st.radio("Navigation", ["Welcome", "Upload and summarize pdf"])
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
                with open('file.pdf', 'wb') as w:
                    w.write(file.getvalue())

                st.info("Please, wait a little bit :) Don't go away from this page")

                reader = Reader('file.pdf')
                summary, links = reader.convert(lang)

                st.title("Ready! Now you can download it")
                st.info(summary)
                st.download_button('Download Summary', summary, file_name="summary.txt")
                
                if len(links) != 0:
                    st.title('Provided links')
                    st.info(*links)