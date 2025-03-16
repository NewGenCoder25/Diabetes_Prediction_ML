import joblib
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load model and scaler
model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler.pkl")

# Custom Styling
st.set_page_config(page_title="Diabetes Risk Checker", page_icon="🩺", layout="wide")

# Sidebar
st.sidebar.header("🩺 Diabetes Risk Prediction")
st.sidebar.write("Move the sliders to input patient details.")

# Input fields using sliders
Pregnancies = st.sidebar.slider("Number of Pregnancies", 0, 20, 1)
Glucose = st.sidebar.slider("Glucose Level", 0, 200, 100)
BloodPressure = st.sidebar.slider("Blood Pressure", 0, 150, 80)
SkinThickness = st.sidebar.slider("Skin Thickness", 0, 100, 20)
Insulin = st.sidebar.slider("Insulin Level", 0, 900, 30)
BMI = st.sidebar.slider("Body Mass Index (BMI)", 0.0, 70.0, 25.0)
DiabetesPedigreeFunction = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
Age = st.sidebar.slider("Age", 0, 120, 30)

# Predict button
if st.sidebar.button("Check Diabetes Risk"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    # Scale input data
    input_data_scaled = scaler.transform(input_data)

    # Get probability of diabetes
    probability = model.predict_proba(input_data_scaled)[0][1]
    threshold = 0.6
    prediction = 1 if probability >= threshold else 0

    # Main Page Output
    st.markdown("<h2 style='text-align: center;'>Prediction Results</h2>", unsafe_allow_html=True)
    
    if prediction == 1:
        st.error(f"🔴 **High Risk: Diabetic**")
    else:
        st.success(f"🟢 **Low Risk: Not Diabetic**")

    # Probability Gauge
    st.write("### **Probability of Diabetes:**")
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.barh(["Diabetes Probability"], [probability], color="red" if prediction == 1 else "green")
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.5, 1])
    st.pyplot(fig)

    # Show probability percentage
    st.write(f"### **Prediction Probability: {probability:.2%}**")

