import streamlit as st
import pickle
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    .survived {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    .not-survived {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🚢 Titanic Survival Predictor")
st.markdown("""
Welcome to the **Titanic Survival Predictor**! This machine learning model predicts whether a passenger would have survived the Titanic disaster based on key features.

Enter the passenger details below and click **Predict** to see the result.
""")

# Sidebar for inputs
st.sidebar.header("Passenger Details")
st.sidebar.markdown("Provide the following information:")

with st.sidebar.form("prediction_form"):
    pclass = st.selectbox("Passenger Class", [1, 2, 3], help="1st class is the highest, 3rd is the lowest.")
    sex = st.selectbox("Sex", ["Male", "Female"])
    age = st.slider("Age", 1, 80, 25, help="Age in years.")
    fare = st.number_input("Fare (in USD)", min_value=0.0, value=50.0, step=0.1, help="Ticket fare paid by the passenger.")
    
    submitted = st.form_submit_button("Predict Survival")

# Convert sex to numerical
sex_num = 1 if sex == "Male" else 0

# Load Model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Prediction logic
if submitted:
    features = np.array([[pclass, sex_num, age, fare]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.markdown('<div class="prediction-box survived">✅ The passenger would have survived!</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown('<div class="prediction-box not-survived">❌ The passenger would not have survived.</div>', unsafe_allow_html=True)
    
    # Display input summary
    st.subheader("Input Summary")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Class", pclass)
    with col2:
        st.metric("Sex", sex)
    with col3:
        st.metric("Age", age)
    with col4:
        st.metric("Fare", f"${fare:.2f}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Machine Learning.")
        