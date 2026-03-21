import streamlit as st
import pickle
import numpy as np
from pathlib import Path

st.title("🚢 Titanic Survival Predictor")

# Load model safely
model_path = Path(__file__).parent / "model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

st.write("Enter passenger details:")

# Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 1, 80, 25)
sibsp = st.slider("Siblings/Spouses aboard", 0, 5, 0)
parch = st.slider("Parents/Children aboard", 0, 5, 0)
fare = st.slider("Fare", 0, 500, 50)

# Convert categorical
sex = 0 if sex == "male" else 1

# Prediction
if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Passenger likely survived")
    else:
        st.error("❌ Passenger likely did NOT survive")

        