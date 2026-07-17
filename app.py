import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="The Performance Ledger",
    page_icon="🎨",
    layout="centered"
)

# --- Handmade Premium Gallery & Interactive Firework Celebration (CSS) ---
st.markdown("""
    <style>
    /* Warm, high-end gallery canvas */
    .stApp {
        background-color: #f7f3ed;
        color: #3d2621;
        font-family: 'Quicksand', system-ui, sans-serif;
    }
    
    /* Elegant Editorial Titles */
    .gallery-title {
        font-family: 'Playfair Display', Georgia, serif;
        color: #721c24 !important; /* Deep Burgundy Crimson */
        font-weight: 700 !important;
        font-size: 2.7rem !important;
        text-align: center;
        margin-bottom: 5px !important;
    }
    
    .gallery-tagline {
        color: #8c7672;
        text-align: center;
        font-style: italic;
        font-size: 1.05rem;
        margin-bottom: 40px;
    }

    /* Hand-Pressed Paper Cards with Gold Hue Highlights */
    .gallery-card {
        background: #ffffff;
        border: 1px solid #e3dcd3;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 
            0 12px 24px -10px rgba(114, 28, 36, 0.12),
            0 1px 4px rgba(0, 0, 0, 0.02);
        position: relative;
    }
    
    .gallery-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: #d4af37; /* Metallic Gold Profile Bar */
        border-radius: 16px 16px 0 0;
    }
    
    .gallery-card h3 {
        color: #721c24 !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 20px !important;
    }

    /* Input Widget Labels Style Adjustments */
    label {
        color: #5c4541 !important;
        font-weight: 600 !important;
    }
    
    /* Tactile Artisanal Button */
    .stButton>button {
        background: linear-gradient(135deg, #721c24 0%, #a93226 100%) !important;
        color: #ffffff !important;
        border: 1px solid #5c1218 !important;
        padding: 14px 28px !important;
        border-radius: 30px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 15px rgba(114, 28, 36, 0.25) !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.01) translateY(-1px);
        box-shadow: 0 6px 20px rgba(114, 28, 36, 0.4) !important;
    }

    /* Craft Scrapbook Celebration Banner */
    .celebration-output {
        background: #fffdfa;
        border: 2px dashed #721c24;
        border-radius: 20px;
        padding: 40px;
        margin-top: 35px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px -15px rgba(0,0,0,0.1);
    }
    
    .output-score {
        font-size: 4.2rem !important;
        font-weight: 800 !important;
        color: #b8860b !important; /* Dark Goldenrod Value */
        margin: 10px 0 15px 0;
        font-family: 'Playfair Display', Georgia, serif;
    }

    /* --- Interactive Celebration Core Elements --- */
    .festive-row {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 25px;
        margin-top: 25px;
        height: 70px;
        position: relative;
    }

    /* Handcrafted Flickering Candles */
    .candle {
        width: 14px;
        height: 45px;
        background: linear-gradient(to bottom, #d4af37, #721c24);
        border-radius: 3px 3px 0 0;
        position: relative;
    }

    .flame {
        width: 10px;
        height: 18px;
        background: radial-gradient(circle at bottom, #ffee55, #f39c12);
        border-radius: 50% 50% 20% 20%;
        position: absolute;
        top: -16px;
        left: 2px;
        animation: sway 0.5s infinite alternate ease-in-out;
    }

    /* Exploding CSS Firecrackers / Sparklers */
    .firecracker {
        width: 8px;
        height: 24px;
        background: #c0392b;
        border-top: 3px solid #f1c40f;
        position: relative;
    }

    .spark {
        position: absolute;
        top: -12px;
        left: -6px;
        width: 20px;
        height: 20px;
        background: radial-gradient(circle, #fff 10%, #ffeb3b 40%, transparent 70%);
        border-radius: 50%;
        animation: burst 0.4s infinite alternate ease-in-out;
    }

    /* Staggering Animation Vectors */
    .festive-row div:nth-child(even) .flame { animation-delay: 0.15s; }
    .festive-row div:nth-child(3) .spark { animation-delay: 0.2s; }
    .festive-row div:nth-child(5) .spark { animation-delay: 0.05s; }

    @keyframes sway {
        0% { transform: scale(1) rotate(-2deg); filter: drop-shadow(0 0 4px #ffee55); }
        100% { transform: scale(1.15) rotate(2deg); filter: drop-shadow(0 0 10px #f39c12); }
    }

    @keyframes burst {
        0% { transform: scale(0.6); opacity: 0.7; }
        100% { transform: scale(1.4); opacity: 1; filter: drop-shadow(0 0 8px #ffeb3b); }
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
st.markdown("<h1 class='gallery-title'>📜 The Learning Ledger</h1>", unsafe_allow_html=True)
st.markdown("<p class='gallery-tagline'>A classic artisanal workspace mapping predictive academic milestones.</p>", unsafe_allow_html=True)

# --- Module 1: Time Log ---
st.markdown('<div class="gallery-card"><h3>📖 Behavioral Profiling</h3>', unsafe_allow_html=True)
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

# --- Module 2: Performance Record ---
st.markdown('<div class="gallery-card"><h3>📊 Performance Vectors</h3>', unsafe_allow_html=True)
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
if st.button("✨ Run Matrix Evaluation", use_container_width=True):
    # Format vectors for unpickled KNN model[cite: 1]
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    try:
        # Generate model prediction[cite: 1]
        prediction = model.predict(features)[0]
        
        # Render the luxury burgundy custom dashboard frame with full animated components
        st.markdown(f"""
            <div class="celebration-output">
                <span style="color: #721c24; font-weight: 700; font-size: 0.95rem; display:block; margin-bottom: 5px; letter-spacing: 0.1em;">✨ EVALUATION VERIFIED SUCCESSFUL ✨</span>
                <span style="color: #8c7672; font-size: 1.1rem;">Projected Evaluation Index</span>
                <h1 class="output-score">{prediction:.2f}</h1>
                
                <!-- Festive Row: Alternate Crackers and Candles Active on Completion -->
                <div class="festive-row">
                    <div class="firecracker"><div class="spark"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="firecracker"><div class="spark"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="firecracker"><div class="spark"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="firecracker"><div class="spark"></div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Something went wrong with the entry evaluation: {e}")
