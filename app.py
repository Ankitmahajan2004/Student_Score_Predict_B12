import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load the trained model safely
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model.pkl: {e}")
    st.stop()

# --- User Interface ---
st.title("🎓 Student Performance Predictor")
st.write("Enter the student's metrics below to estimate their performance index using the KNN Regression model.")
st.markdown("---")

# Organized layout using Streamlit columns
col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "Study Hours per Week", 
        min_value=0.0, 
        max_value=168.0, 
        value=10.0, 
        step=0.5,
        help="Total number of hours spent studying per week."
    )
    
    sleep_hours = st.number_input(
        "Average Sleep Hours", 
        min_value=0.0, 
        max_value=24.0, 
        value=7.0, 
        step=0.5,
        help="Average daily sleep hours."
    )

with col2:
    attendance_percent = st.slider(
        "Attendance Rate (%)", 
        min_value=0.0, 
        max_value=100.0, 
        value=85.0, 
        step=1.0,
        help="Overall class attendance percentage."
    )
    
    previous_scores = st.number_input(
        "Previous Exam Score", 
        min_value=0.0, 
        max_value=100.0, 
        value=70.0, 
        step=1.0,
        help="The score achieved in the most recent examination."
    )

st.markdown("---")

# --- Prediction Logic ---
if st.button("Predict Performance", type="primary", use_container_width=True):
    # Prepare the input array in the exact order expected by the model
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Generate prediction
        prediction = model.predict(features)[0]
        
        # Display results cleanly
        st.success("### Prediction Complete!")
        
        # Metric dashboard view
        st.metric(
            label="Estimated Final Performance Score", 
            value=f"{prediction:.2f}"
        )
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
