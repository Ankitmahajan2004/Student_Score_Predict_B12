import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="EduPredict Pro AI",
    page_icon="🔮",
    layout="centered"
)

# --- Cyberpunk Midnight & Emerald Mint Theme ---
st.markdown("""
    <style>
    /* Base Application Overrides */
    .stApp {
        background: radial-gradient(circle at 50% 15%, #050b14 0%, #020408 100%);
        color: #f1f5f9;
    }
    
    /* Header Typography with Emerald Gradient */
    .hero-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-weight: 800 !important;
        font-size: 2.8rem !important;
        text-align: center;
        background: linear-gradient(135deg, #2dd4bf 0%, #10b981 50%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px !important;
        letter-spacing: -0.05em;
    }
    
    .hero-subtitle {
        color: #64748b;
        text-align: center;
        font-size: 1.05rem;
        margin-bottom: 40px;
        font-weight: 400;
        letter-spacing: 0.02em;
    }

    /* Structured Tech Panels with Mint Glow Shadows */
    .tech-panel {
        background: rgba(10, 25, 47, 0.7);
        border: 1px solid rgba(45, 212, 191, 0.1);
        border-radius: 20px;
        padding: 32px;
        margin-bottom: 28px;
        box-shadow: 
            0 4px 20px -2px rgba(0, 0, 0, 0.7), 
            0 0 15px rgba(16, 185, 129, 0.03),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .tech-panel:hover {
        border-color: rgba(45, 212, 191, 0.4);
        box-shadow: 
            0 20px 30px -5px rgba(0, 0, 0, 0.8), 
            0 0 25px rgba(45, 212, 191, 0.15);
        transform: translateY(-2px);
    }
    
    .tech-panel h3 {
        color: #e2e8f0 !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 24px !important;
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    /* Input Widget Labels Style Customization */
    label {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.03em;
    }
    
    /* High-Impact Interactive Run Button */
    .stButton>button {
        background: linear-gradient(90deg, #0d9488 0%, #10b981 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(45, 212, 191, 0.3) !important;
        padding: 14px 28px !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        letter-spacing: 0.05em !important;
        box-shadow: 0 4px 20px 0 rgba(16, 185, 129, 0.25) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.01);
        box-shadow: 0 6px 25px 0 rgba(45, 212, 191, 0.5) !important;
        border-color: #2dd4bf !important;
    }

    /* Floating Vivid Mint Output Dashboard Card */
    .cosmic-output {
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.3) 0%, rgba(2, 4, 8, 0.9) 100%);
        border: 2px solid #10b981;
        border-radius: 24px;
        padding: 40px;
        margin-top: 35px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 30px rgba(16, 185, 129, 0.15);
    }
    
    .metric-value {
        font-size: 4.8rem !important;
        font-weight: 900 !important;
        line-height: 1 !important;
        background: linear-gradient(135deg, #ffffff 30%, #2dd4bf 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 15px 0 0 0;
        filter: drop-shadow(0 0 15px rgba(45, 212, 191, 0.4));
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
st.markdown("<h1 class='hero-title'>🔮 EduPredict Pro AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Smart Machine Learning Intelligence Hub for Student Success Performance Metrics</p>", unsafe_allow_html=True)

# --- Panel 1: Input Cluster Alpha ---
st.markdown('<div class="tech-panel"><h3>⏰ Routine & Lifestyle Profiling</h3>', unsafe_allow_html=True)
hours_studied = st.number_input(
    "📚 Weekly Study Duration (Hours)", 
    min_value=0.0, 
    max_value=168.0, 
    value=10.0, 
    step=0.5,
    help="Total logged hours dedicated strictly to self-study per week."
)
sleep_hours = st.number_input(
    "😴 Daily Sleep Allocation (Hours/Night)", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.0, 
    step=0.5,
    help="Average sleep hours per 24-hour cycle."
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Panel 2: Input Cluster Beta ---
st.markdown('<div class="tech-panel"><h3>🎯 Historical Performance Data</h3>', unsafe_allow_html=True)
attendance_percent = st.slider(
    "🏫 Classroom Attendance Ratio (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=85.0, 
    step=1.0,
    help="Verified presence metrics across all required learning modules."
)
previous_scores = st.number_input(
    "🥇 Prior Exam Baseline Score", 
    min_value=0.0, 
    max_value=100.0, 
    value=70.0, 
    step=1.0,
    help="The aggregate raw performance index scored during the prior evaluation window."
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Execution Core ---
if st.button("🚀 EXECUTE PREDICTIVE INTELLIGENCE", use_container_width=True):
    # Construct raw data arrays[cite: 1]
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Run inference matrix[cite: 1]
        prediction = model.predict(features)[0]
        
        # Render the luxury floating emerald target dashboard display
        st.markdown(f"""
            <div class="cosmic-output">
                <span style="color: #2dd4bf; font-weight: 700; font-size: 0.9rem; letter-spacing: 0.2em; display:block; margin-bottom: 8px; text-transform: uppercase;">✨ ANALYSIS COMPLETION SUCCESSFUL ✨</span>
                <span style="color: #94a3b8; font-size: 1.15rem; font-weight: 400;">📊 Estimated Student Performance Index</span>
                <h1 class="metric-value">{prediction:.2f}</h1>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"⚠️ Execution core failure: {e}")
