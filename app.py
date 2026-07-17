import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for modern vertical layout, shadow effects, and color combinations
st.markdown("""
    <style>
    /* Main application background and font tweak */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Title style adjustments */
    h1 {
        color: #1e3a8a !important; /* Deep Navy Blue */
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 5px !important;
    }
    
    .subtitle-text {
        color: #4b5563; /* Slate Gray */
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.1rem;
    }

    /* Card styling for the vertical layout blocks */
    .feature-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }
    
    .feature-card h3 {
        color: #2563eb !important; /* Royal Blue */
        margin-top: 0 !important;
        margin-bottom: 15px !important;
        font-size: 1.25rem !important;
    }

    /* Result Card styling */
    .result-card {
        background-color: #f0fdf4; /* Very light mint/green */
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #16a34a; /* Vibrant Green border accent */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        margin-top: 25px;
        text-align: center;
    }
    </style>
""", unsafe_styled_html=True)

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

# --- Title Header ---
st.markdown("<h1>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Input the metrics below to vertically analyze and estimate final performance index scores.</p>", unsafe_allow_html=True)

# --- Vertical Card 1: Time Allocations ---
st.markdown('<div class="feature-card"><h3>🕒 Time Management</h3>', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# --- Vertical Card 2: Academic Standings ---
st.markdown('<div class="feature-card"><h3>📈 Academic Metrics</h3>', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# --- Prediction Action ---
if st.button("Predict Performance Index", type="primary", use_container_width=True):
    # Prepare the input array in the exact order expected by the model
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Generate prediction
        prediction = model.predict(features)[0]
        
        # Display results cleanly inside the stylized green-bordered shadow card
        st.markdown(f"""
            <div class="result-card">
                <span style="color: #16a34a; font-weight: 600; font-size: 1.1rem; display:block; margin-bottom: 8px;">Prediction Matrix Computed Successfully</span>
                <span style="color: #1f2937; font-size: 0.95rem;">Estimated Performance Score</span>
                <h2 style="color: #15803d; margin: 5px 0 0 0; font-size: 2.2rem; font-weight: 800;">{prediction:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
