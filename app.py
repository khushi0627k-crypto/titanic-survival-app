import streamlit as st
import pickle
import numpy as np

# ---------------- UI ----------------
st.title("🚢 Titanic Survival Prediction")

st.write("Enter passenger details:")

# Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 1, 80, 25)
fare = st.number_input("Fare", value=50.0)

# Convert sex
sex = 1 if sex == "Male" else 0

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# ---------------- Prediction ----------------
if st.button("Predict"):
    features = np.array([[pclass, sex, age, fare]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")
        