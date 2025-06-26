import streamlit as st
import pickle
import numpy as np
import pandas as pd


with open("svm_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="📘 Marks Prediction", layout="centered")
st.title("📚 Predict Marks using Trained SVM Model")

st.markdown("Enter the study details below to see predicted exam marks:")


number_courses = st.number_input("📓 Number of Courses", min_value=1, step=1)
time_study = st.number_input("⏱️ Study Time (Hours per Day)", min_value=0.0, step=0.5)


input_data = pd.DataFrame([[number_courses, time_study]], columns=['number_courses', 'time_study'])
input_scaled = scaler.transform(input_data)
prediction = model.predict(input_scaled)[0]


st.success(f"🎯 Predicted Marks: {prediction:.2f}")
