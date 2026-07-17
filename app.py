import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Core Analytics Hub",
    page_icon="🔮",
    layout="centered"
)

# --- Elite Custom Tech Theme & Layout (CSS) ---
st.markdown("""
    <style>
    /* Base Application Overrides */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #111827 0%, #030712 100%);
        color: #f3f4f6;
    }
    
    /* Header Typography */
    .hero-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-weight: 800 !important;
        font-size: 3rem !important;
        text-align: center;
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 50%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px !important;
        letter-spacing: -0.06em;
    }
    
    .hero-subtitle {
        color: #6b7280;
        text-align: center;
        font-size: 1.05rem;
        margin-bottom: 45px;
        font-weight: 400;
        letter-spacing: 0.02em;
    }

    /* Structured Tech Panels with Multi-Layered Glow Shadows */
    .tech-panel {
        background: rgba(17, 24, 39, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 32px;
        margin-bottom: 28px;
        box-shadow: 
            0 4px 6px -1px rgba(0, 0, 0, 0.5), 
            0 10px 15px -3px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .tech-panel:hover {
        border-color: rgba(167, 139, 250, 0.4);
        box-shadow: 
            0 20px 25px -5px rgba(0, 0, 0, 0.6), 
            0 0 20px rgba(167, 139, 250, 0.15),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .tech-panel h3 {
        color: #e5e7eb !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 24px !important;
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .tech-panel h3::before {
        content: '';
        display: inline-block;
        width: 4px;
        height: 16px;
        background: #a78bfa;
        border-radius: 2px;
    }

    /* Streamlit Global Widget Color Tuning */
    label {
        color: #9ca3af !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Interactive Run Button Customization */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #a78bfa 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.4) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.01);
        box-shadow: 0 6px 20px 0 rgba(167, 139, 250, 0.6) !important;
    }

    /* Floating Cosmic Output Dashboard Card */
    .cosmic-output {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.9) 0%, rgba(31, 41, 55, 0.8) 100%);
        border: 1px solid rgba(167, 139, 250, 0.3);
        border-radius: 24px;
        padding: 40px;
        margin-top: 35px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }
    
    .cosmic-output::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(167, 139, 250, 0.08) 0%, transparent 60%);
        pointer-events: none;
    }
    
    .metric-value {
        font-size: 4.5rem !important;
        font-weight: 900 !important;
        line-height: 1 !important;
        background: linear-gradient(135deg, #ffffff 0%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 15px 0 0 0;
        filter: drop-shadow(0 0 15px rgba(192, 132, 252, 0.3));
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
    st.error(f"Error loading model: {e}")
    st.stop()

# --- Structural Header ---
st.markdown("<h1 class='hero-title'>🔮 Core Predictive Engine</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>High-precision analytical matrix utilizing unpickled regression variables.</p>", unsafe_allow_html=True)

# --- Panel 1: Input Cluster Alpha ---
st.markdown('<div class="tech-panel"><h3>Behavioral Profiling</h3>', unsafe_allow_html=True)
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

# --- Panel 2: Input Cluster Beta ---
st.markdown('<div class="tech-panel"><h3>Performance Metrics</h3>', unsafe_allow_html=True)
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

# --- Execution Core ---
if st.button("RUN PREDICTIVE INFERENCE", use_container_width=True):
    # Construct raw data arrays
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Run inference matrix
        prediction = model.predict(features)[0]
        
        # Render the luxury floating target dashboard display
        st.markdown(f"""
            <div class="cosmic-output">
                <span style="color: #a78bfa; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.2em; display:block; margin-bottom: 8px; text-transform: uppercase;">Inference Successful</span>
                <span style="color: #9ca3af; font-size: 1.1rem; font-weight: 400;">Projected Student Performance Rating</span>
                <h1 class="metric-value">{prediction:.2f}</h1>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Execution core failure: {e}")
