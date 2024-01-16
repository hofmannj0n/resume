from pathlib import Path
import streamlit as st
from PIL import Image


profile_pic = "/Users/jonathanhofmann/Desktop/programming/resume-streamlit/IMG_9300.jpeg"
resume_file = "/Users/jonathanhofmann/Desktop/programming/resume-streamlit/Hofmann_Jonathan.cv.pdf"
css_file = "/Users/jonathanhofmann/Desktop/programming/resume-streamlit/main.css"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jonathan Hofmann"
PAGE_ICON = ":wave:"
NAME = "Jon Hofmann"
DESCRIPTION = """
Recently, I have been exploring machine learning use cases & building practical applications.
"""
EMAIL = "JChofmann99@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCoE0MAtX0RaT9Dlf_uu01mg",
    "LinkedIn": "https://www.linkedin.com/in/jonathan-hofmann-67200b1b2/",
    "GitHub": "https://github.com/hofmannj0n",
}
PROJECTS = {
    "🏆 Feather - Data management service designed for bars and restaurants": "https://youtu.be/LzCfNanQ_9c",
    "🏆 Deep Learning Medical Image Analysis - Semantic segmentation model to identify brain damage in CT scans": "https://pythonandvba.com/mytoolbelt/",
    "🏆 Automated Machine Learning - Comparing ARIMA models on stock market data": "https://youtu.be/Sb0A9i6d320",
    "🏆 Algorithmic Trading - Trading strategies to automate Financial Decision Making": "https://youtu.be/3egaMfE9388",
}


# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="large")
with col1:
    st.image(profile_pic)

with col2:
    st.header(NAME, divider='rainbow')
    st.write(":wave: Hi! I'm Jon, a Data Scientist from San Diego, California.")
    st.write(DESCRIPTION)
    st.divider()
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📱", "703-304-7468")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")