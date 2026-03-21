import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚢 Titanic Survival Predictor")

st.write("Enter passenger details:")

# Inputs
Pclass = st.selectbox("Passenger Class", [1,2,3])
Sex = st.selectbox("Sex", ["male","female"])
Age = st.number_input("Age", 1, 80, 25)
Fare = st.number_input("Fare", 0.0, 500.0, 50.0)

# convert sex
Sex = 0 if Sex == "male" else 1

# prediction
if st.button("Predict"):
    features = np.array([[Pclass, Sex, Age, Fare]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")

        