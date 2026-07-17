import streamlit as st
import pickle
import numpy as np

# Set up page configuration with a warm look
st.set_page_config(
    page_title="Student Growth Analytics",
    page_icon="📝",
    layout="centered"
)

# --- Handmade Studio & Organic Celebration Theme (CSS) ---
st.markdown("""
    <style>
    /* Premium off-white/cream textured background */
    .stApp {
        background-color: #faf6f0;
        color: #2e2c29;
        font-family: 'Quicksand', 'Nunito', system-ui, sans-serif;
    }
    
    /* Elegant Editorial Typography */
    .studio-title {
        font-family: 'Playfair Display', Georgia, serif;
        color: #c95a49 !important; /* Muted Terracotta */
        font-weight: 700 !important;
        font-size: 2.6rem !important;
        text-align: center;
        margin-bottom: 5px !important;
    }
    
    .studio-tagline {
        color: #7c756b;
        text-align: center;
        font-style: italic;
        font-size: 1.1rem;
        margin-bottom: 35px;
    }

    /* Hand-Crafted Premium Paper Cards */
    .studio-card {
        background: #ffffff;
        border: 1px solid #e6dfd5;
        border-radius: 14px;
        padding: 28px;
        margin-bottom: 25px;
        box-shadow: 
            0 10px 30px -15px rgba(139, 126, 116, 0.2),
            0 1px 3px rgba(0, 0, 0, 0.02);
        position: relative;
    }
    
    .studio-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: #e8c595; /* Soft Ochre Sand accent */
        border-radius: 14px 14px 0 0;
    }
    
    .studio-card h3 {
        color: #4a4741 !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 20px !important;
        letter-spacing: -0.01em;
    }

    /* Softening Streamlit Labels for a Human Accent */
    label {
        color: #5c5750 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    /* Tactile Studio Craft Button */
    .stButton>button {
        background-color: #c95a49 !important;
        color: #ffffff !important;
        border: 2px solid #b54a3a !important;
        padding: 12px 24px !important;
        border-radius: 30px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(201, 90, 73, 0.2) !important;
    }
    
    .stButton>button:hover {
        background-color: #b54a3a !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(201, 90, 73, 0.35) !important;
    }

    /* Elegant Custom Scrapbook Output Frame */
    .handmade-output {
        background: #fdfbf7;
        border: 2px dashed #d1c7bd;
        border-radius: 16px;
        padding: 35px;
        margin-top: 30px;
        text-align: center;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .output-value {
        font-size: 4rem !important;
        font-weight: 800 !important;
        color: #2b5c47 !important; /* Deep Sage Green */
        margin: 10px 0 15px 0;
        font-family: 'Playfair Display', Georgia, serif;
    }

    /* --- Animated CSS Celebration Candles Container --- */
    .candle-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }

    .candle {
        width: 15px;
        height: 50px;
        background: linear-gradient(to bottom, #e8c595, #c95a49);
        border-radius: 4px 4px 0 0;
        position: relative;
    }

    .flame {
        width: 12px;
        height: 20px;
        background: radial-gradient(circle at bottom, #ffdf00, #ff5722);
        border-radius: 50% 50% 20% 20%;
        position: absolute;
        top: -18px;
        left: 1.5px;
        animation: flicker 0.6s infinite alternate ease-in-out;
        box-shadow: 0 0 10px rgba(255, 87, 34, 0.5);
    }

    /* Give candles staggered flickering effects */
    .candle:nth-child(2) .flame { animation-delay: 0.1s; }
    .candle:nth-child(3) .flame { animation-delay: 0.25s; }
    .candle:nth-child(4) .flame { animation-delay: 0.15s; }
    .candle:nth-child(5) .flame { animation-delay: 0.3s; }

    @keyframes flicker {
        0% { transform: scale(1) rotate(-1deg); opacity: 0.9; }
        100% { transform: scale(1.15) rotate(1deg); opacity: 1; filter: drop-shadow(0 0 8px #ffdf00); }
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

# --- Title Header ---
st.markdown("<h1 class='studio-title'>🎨 The Learning Ledger</h1>", unsafe_allow_html=True)
st.markdown("<p class='studio-tagline'>A carefully calibrated environment forecasting academic trajectory outcomes.</p>", unsafe_allow_html=True)

# --- Module 1: Time & Wellness Log ---
st.markdown('<div class="studio-card"><h3>🌿 Time & Wellness Profiles</h3>', unsafe_allow_html=True)
hours_studied = st.number_input(
    "📚 Weekly Study Allocation (Hours)", 
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

# --- Module 2: Institutional Standing ---
st.markdown('<div class="studio-card"><h3>📊 Classroom Performance Record</h3>', unsafe_allow_html=True)
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

# --- Inference Button ---
if st.button("✨ Evaluate Student Trajectory", use_container_width=True):
    # Format vectors for unpickled KNN model[cite: 1]
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Generate model prediction[cite: 1]
        prediction = model.predict(features)[0]
        
        # Display the custom handmade scrapbook style output + candle celebration block
        st.markdown(f"""
            <div class="handmade-output">
                <span style="color: #7c756b; font-weight: 600; font-size: 0.95rem; display:block; margin-bottom: 5px;">✨ Evaluation Successfully Logged ✨</span>
                <span style="color: #4a4741; font-size: 1.1rem; font-weight: 400;">Projected Performance Index</span>
                <h1 class="output-value">{prediction:.2f}</h1>
                
                <!-- Celebration Candles Rendering Triggered Upon Result -->
                <div class="candle-container">
                    <div class="candle"><div class="flame"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Something went wrong with the entry evaluation: {e}")
