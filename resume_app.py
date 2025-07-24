# app.py

import streamlit as st
import pandas as pd

df = pd.read_csv(r"c:\Users\dekny\OneDrive\Desktop\Resume Parser\UpdatedResumeDataSet.csv")


def classify_resume(text):
    required_skills = ['python', 'machine learning', 'nlp']
    if all(skill in text.lower() for skill in required_skills):
        return 'Meets'
    return 'Does Not Meet'

st.title("Resume Qualification Classifier")

selected_index = st.slider("Select resume index", 0, len(df)-1)
resume_text = df.iloc[selected_index]['Resume']
st.text_area("Resume Text", resume_text, height=300)

result = classify_resume(resume_text)
st.subheader(f"Result: {result}")

