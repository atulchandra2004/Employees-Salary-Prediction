import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")

years = st.number_input("Enter Years of Experience", value=1)
jobrate = st.number_input("Enter Job Rate", value=3.5)

X = [years, jobrate]

model = joblib.load("Linearmodel.pkl")

if st.button("Predict"):
    X1 = np.array([X])
    prediction = model.predict(X1)
    st.success(f"Predicted Salary: {prediction[0]}")

import streamlit as st
import joblib
import numpy as np

st.title("💰 Salary Prediction App")

model = joblib.load("Linearmodel.pkl")

years = st.number_input(
    "Years of Experience",
    min_value=0,
    value=1,
    step=1
)

jobrate = st.number_input(
    "Job Rating",
    min_value=0.0,
    max_value=5.0,
    value=3.5,
    step=0.5
)

if st.button("Predict Salary"):
    X = np.array([[years, jobrate]])
    prediction = model.predict(X)
    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")