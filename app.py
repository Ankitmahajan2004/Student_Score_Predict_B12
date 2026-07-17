import streamlit as st
import pickle
import numpy as np

# Set up stunning dark dashboard page configuration
st.set_page_config(
    page_title="Academic Intelligence Dashboard",
    page_icon="⚡",
    layout="centered"
)

# --- High-End Executive Dashboard Theme (CSS) ---
st.markdown("""
    <style>
    /* Global Application Theme Override */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Sleek Title Design */
    .dashboard-title {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        font-size: 2.8rem !important;
        text-align: center;
        margin-bottom: 5px !important;
        letter-spacing: -0.05em;
    }
    
    .dashboard-tagline {
        color: #94a3b8;
        text-align: center;
        margin-bottom: 40px;
        font-size: 1.1rem;
        font-weight: 400;
    }

    /* Glassmorphic Vertical Input Cards with Glow Shadows */
    .dashboard-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 28px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .dashboard-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.5), 0 0 15px rgba(56, 189, 248, 0.15);
        border: 1px solid rgba(56, 189, 248, 0.3);
    }
    
    .dashboard-card h3 {
        background: linear-gradient(90deg, #f1f5f9, #cbd5e1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 0 !important;
        margin-bottom: 20px !important;
        font-size: 1.35rem !important;
        font-weight: 600 !important;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Streamlit Input Label Adjustments for Dark Mode Visibility */
    label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }

    /* Futuristic Neon Result Card */
    .neon-result-card {
        background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.15), rgba(15, 23, 42, 0.8));
        padding: 30px;
        border-radius: 16px;
        border: 2px solid #38bdf8;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.25), inset 0 0 15px rgba(56, 189, 248, 0.05);
        margin-top: 30px;
        text-align: center;
        animation: pulse 2s infinite alternate;
    }
    
    .result-value {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #38bdf8 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0 0 0;
        text-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

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

# --- Dashboard Header ---
st.markdown("<h1 class='dashboard-title'>⚡ A.I. Student Analytics Engine</h1>", unsafe_allow_html=True)
st.markdown("<p class='dashboard-tagline'>Predictive Machine Learning Framework for Student Trajectory Performance [KNN-Regression v1.6.1]</p>", unsafe_allow_html=True)

# --- Vertical Block 1: Habits & Routines ---
st.markdown('<div class="dashboard-card"><h3>⏳ Lifestyle & Time Allocation</h3>', unsafe_allow_html=True)
hours_studied = st.number_input(
    "Weekly Study Allocation (Hours)", 
    min_value=0.0, 
    max_value=168.0, 
    value=10.0, 
    step=0.5,
    help="Total logged hours dedicated strictly to self-study per week."
)
sleep_hours = st.number_input(
    "Diurnal Rest Cycle (Hours/Night)", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.0, 
    step=0.5,
    help="Average sleep hours per 24-hour cycle."
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Vertical Block 2: Performance Vectors ---
st.markdown('<div class="dashboard-card"><h3>📊 Institutional Performance Metrics</h3>', unsafe_allow_html=True)
attendance_percent = st.slider(
    "Classroom Attendance Rate (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=85.0, 
    step=1.0,
    help="Verified presence metrics across all required learning modules."
)
previous_scores = st.number_input(
    "Baseline Evaluation Index (Last Exam)", 
    min_value=0.0, 
    max_value=100.0, 
    value=70.0, 
    step=1.0,
    help="The aggregate raw performance index scored during the prior evaluation window."
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Dashboard Action Trigger ---
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
if st.button("🚀 EXECUTE PREDICTIVE ENGINE", type="primary", use_container_width=True):
    # Form input vectors
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Infer target variable from unpickled KNN Regressor model
        prediction = model.predict(features)[0]
        
        # Display the sleek neon metric card
        st.markdown(f"""
            <div class="neon-result-card">
                <span style="color: #38bdf8; font-weight: 700; font-size: 0.9rem; letter-spacing: 0.15em; display:block; margin-bottom: 5px; text-transform: uppercase;">Inference Analytics Computed</span>
                <span style="color: #94a3b8; font-size: 1.05rem; font-weight: 400;">Projected Student Performance Index</span>
                <h1 class="result-value">{prediction:.2f}</h1>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Execution core failure: {e}")
