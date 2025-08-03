import streamlit as st
import joblib
import numpy as np

# Load the trained model
model=joblib.load('bmi_model.joblib')

# Set page configuration
st.set_page_config(page_title="BMI Calculator", layout="centered")

st.title("BMI Calculator")

# Input fields
gender = st.selectbox("Select your Gender", ["Male", "Female"])
height = st.number_input("Enter your Height (in cm)")
weight = st.number_input("Enter your Weight (in kg)")

# Button
if st.button("Predict BMI Category"):
    # Encode gender manually
    if gender == "Male":
        gender_encoded = 1  
    else:
        gender_encoded = 0

    # Make sure input is float
    input_data = np.array([[gender_encoded, float(height), float(weight)]], dtype=float)

    # Predict
    prediction = model.predict(input_data)

    # Mapping index to category
    labels = {
        0: "Extremely Weak",
        1: "Weak",
        2: "Normal",
        3: "Overweight",
        4: "Obesity",
        5: "Extreme Obesity"
    }

    label = labels.get(prediction[0], "Unknown Category")
    st.success(f"Based on your input, your BMI category is: **{label}**")
