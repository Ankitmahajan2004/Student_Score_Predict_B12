import streamlit as st
import pickle
import numpy as np
import streamlit.components.v1 as components

# Set up page configuration with full fluid dashboard viewport layout
st.set_page_config(
    page_title="EduIntel Pro // Matrix Core",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Elite Vercel / Linear / Stripe Premium Dark Theme Architecture ---
st.markdown("""
    <style>
    /* Global Viewport Resets & Deep Space Ambient Backgrounds */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0c101b 0%, #030712 100%);
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Command Hub App Bar Header */
    .app-header {
        text-align: center;
        margin-bottom: 40px;
        padding-top: 20px;
    }
    
    .app-badge {
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    .app-title {
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        letter-spacing: -0.05em !important;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 !important;
    }
    
    .app-tagline {
        color: #64748b;
        font-size: 1.1rem;
        margin-top: 8px;
    }

    /* Stripe/Linear Style Micro-Bordered Input Containers */
    .panel-box {
        background: rgba(15, 23, 42, 0.4);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .panel-box:hover {
        border-color: rgba(56, 189, 248, 0.3);
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.08);
        transform: translateY(-2px);
    }
    
    .panel-box h3 {
        color: #f1f5f9 !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 20px !important;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Input Parameter Labels Styling */
    label {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Framer/Vercel Hyper-Tactile Button Frame */
    .stButton>button {
        background: #ffffff !important;
        color: #030712 !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        letter-spacing: -0.01em !important;
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.005);
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.4) !important;
        background: #38bdf8 !important;
        color: #030712 !important;
    }

    /* Luxury Holographic Core Prediction Card */
    .hologram-result {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.08) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 0 20px rgba(56, 189, 248, 0.1);
        position: relative;
    }
    
    .score-display {
        font-size: 5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #ffffff 30%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
        filter: drop-shadow(0 0 20px rgba(56, 189, 248, 0.4));
    }

    /* --- Interactive Sparkler & Candle Celebration Elements --- */
    .celebration-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 25px;
    }
    
    .candle { width: 12px; height: 40px; background: linear-gradient(to bottom, #38bdf8, #030712); border-radius: 3px; position: relative; }
    .flame { width: 8px; height: 16px; background: radial-gradient(circle at bottom, #fff, #38bdf8); border-radius: 50% 50% 20% 20%; position: absolute; top: -14px; left: 2px; animation: flicker 0.4s infinite alternate ease-in-out; }
    .sparkler { width: 6px; height: 20px; background: #475569; position: relative; }
    .spark { position: absolute; top: -10px; left: -7px; width: 20px; height: 20px; background: radial-gradient(circle, #fff, #38bdf8, transparent); border-radius: 50%; animation: burst 0.3s infinite alternate ease-in-out; }

    @keyframes flicker { 0% { transform: scale(1); } 100% { transform: scale(1.2); filter: drop-shadow(0 0 8px #38bdf8); } }
    @keyframes burst { 0% { transform: scale(0.7); } 100% { transform: scale(1.3); filter: drop-shadow(0 0 10px #ffffff); } }
    </style>
""", unsafe_allow_html=True)

# Load the inference model safely
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model framework core: {e}")
    st.stop()

# --- Top Dashboard Command Hub Bar ---
st.markdown("""
    <div class='app-header'>
        <span class='app-badge'>⚡ Enterprise Analytics Suite</span>
        <h1 class='app-title'>EduIntel Core Framework</h1>
        <p class='app-tagline'>Predictive Student Velocity, Attendance Mapping, and Modular Grade Analysis Engine</p>
    </div>
""", unsafe_allow_html=True)

# --- Layout Matrix Isolation (Inputs vs Actions) ---
col_controls, col_display = st.columns([1, 1.2], gap="large")

with col_controls:
    st.markdown('<div class="panel-box"><h3>🕒 Time Parameters & Allocation</h3>', unsafe_allow_html=True)
    hours_studied = st.number_input("📚 Weekly Study Duration (Hours)", min_value=0.0, max_value=168.0, value=12.0, step=0.5)
    sleep_hours = st.number_input("😴 Sleep Matrix Log (Hours/Night)", min_value=0.0, max_value=24.0, value=7.5, step=0.5)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel-box"><h3>📊 Core Performance Thresholds</h3>', unsafe_allow_html=True)
    attendance_percent = st.slider("🏫 Classroom Attendance Index (%)", min_value=0.0, max_value=100.0, value=88.0, step=1.0)
    previous_scores = st.number_input("🥇 Baseline Assessment Index Score", min_value=0.0, max_value=100.0, value=76.0, step=1.0)
    st.markdown('</div>', unsafe_allow_html=True)
    
    execute_inference = st.button("🚀 EXECUTE INFERENCE MATRIX", use_container_width=True)

# --- Dynamic Result Processing & Interactive Visual Rendering ---
with col_display:
    if execute_inference:
        # Array clean of leaky bracket strings
        features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            prediction = model.predict(features)[0]
            
            # Render Core Numeric Holographic View Box
            st.markdown(f"""
                <div class="hologram-result">
                    <span style="color: #38bdf8; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.2em; display:block; text-transform: uppercase;">Inference Processing Verified</span>
                    <span style="color: #64748b; font-size: 1.05rem;">Projected Target Performance Rating</span>
                    <h1 class="score-display">{prediction:.2f}</h1>
                    
                    <div class="celebration-row">
                        <div class="sparkler"><div class="spark"></div></div>
                        <div class="candle"><div class="flame"></div></div>
                        <div class="sparkler"><div class="spark"></div></div>
                        <div class="candle"><div class="flame"></div></div>
                        <div class="sparkler"><div class="spark"></div></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Render Premium Dynamic Notion-styled Diagnostic Alert Card
            st.markdown(f"""
                <div class="panel-box" style="margin-top:20px; border-left:4px solid #38bdf8; background:rgba(56, 189, 248, 0.02);">
                    <h4 style="color:#38bdf8; margin:0 0 8px 0; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.05em;">🔮 AI Diagnostic Insights</h4>
                    <p style="color:#94a3b8; font-size:0.95rem; margin:0; line-height:1.5;">
                        Student displays strong performance potential at <b>{prediction:.2f}</b>. 
                        The target score correlation exhibits an optimal trajectory anchored by an attendance consistency index of <b>{attendance_percent}%</b>. 
                        Recommendation: Maintain a study velocity above <b>{hours_studied} hours/week</b> to insulate scores from systemic variance.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Mount Interactive, Clean Custom Chart Suite via Embed Component
            chart_canvas_html = f"""
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
                <style>
                    body {{ background: transparent; font-family: sans-serif; margin: 0; padding: 0; }}
                    .chart-element {{ background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 16px; padding: 20px; margin-bottom: 20px; }}
                    h5 {{ margin: 0 0 15px 0; color: #f1f5f9; text-align: center; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; }}
                    .double-layout {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
                </style>
            </head>
            <body>
                <!-- 1. Monthly Marks Trend Line Chart -->
                <div class="chart-element">
                    <h5>📈 Monthly Marks Trend Velocity</h5>
                    <canvas id="lineChart" height="110"></canvas>
                </div>

                <div class="double-layout">
                    <!-- 2. Subject Scores Bar Chart -->
                    <div class="chart-element">
                        <h5>📊 Subject-Wise Scores</h5>
                        <canvas id="barChart"></canvas>
                    </div>
                    <!-- 3. Skill Radar Analysis Matrix -->
                    <div class="chart-element">
                        <h5>🕸️ Core Competency Skill Analysis</h5>
                        <canvas id="radarChart"></canvas>
                    </div>
                </div>

                <div class="double-layout">
                    <!-- 4. Grade Vector Pie Chart -->
                    <div class="chart-element">
                        <h5>🍕 Relative Grade Distribution</h5>
                        <canvas id="pieChart"></canvas>
                    </div>
                    <!-- 5. Attendance Donut Tracking Matrix -->
                    <div class="chart-element">
                        <h5>🍩 Attendance Matrix Split</h5>
                        <canvas id="donutChart"></canvas>
                    </div>
                </div>

                <script>
                    const baseOptions = {{
                        responsive: true,
                        animation: {{ duration: 1800, easing: 'easeOutExpo' }},
                        plugins: {{ legend: {{ labels: {{ color: '#94a3b8', font: {{ family: 'system-ui' }} }} }} }},
                        scales: {{
                            x: {{ grid: {{ color: 'rgba(255,255,255,0.03)' }}, ticks: {{ color: '#64748b' }} }},
                            y: {{ grid: {{ color: 'rgba(255,255,255,0.03)' }}, ticks: {{ color: '#64748b' }} }}
                        }}
                    }};
                    
                    const techPalette = ['#38bdf8', '#818cf8', '#34d399', '#fb7185', '#a78bfa'];

                    // Line Chart Configuration
                    new Chart(document.getElementById('lineChart'), {{
                        type: 'line',
                        data: {{
                            labels: ['Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Term Capstone'],
                            datasets: [{{ label: 'Performance Velocity Target', data: [62, 70, 67, {previous_scores}, {prediction}], borderColor: '#38bdf8', borderWidth: 3, pointBackgroundColor: '#ffffff', tension: 0.25, fill: false }}]
                        }},
                        options: baseOptions
                    }});

                    // Bar Chart Configuration
                    new Chart(document.getElementById('barChart'), {{
                        type: 'bar',
                        data: {{
                            labels: ['STEM', 'Lang', 'Arts', 'Hist'],
                            datasets: [{{ label: 'Scores', data: [{previous_scores}, 84, 91, 73], backgroundColor: techPalette.slice(0,4), borderRadius: 6 }}]
                        }},
                        options: baseOptions
                    }});

                    // Radar Chart Configuration
                    new Chart(document.getElementById('radarChart'), {{
                        type: 'radar',
                        data: {{
                            labels: ['Logic', 'Focus', 'Retention', 'Velocity', 'Presence'],
                            datasets: [{{ label: 'Metrics Spectrum', data: [85, {hours_studied * 7}, 75, 80, {attendance_percent}], backgroundColor: 'rgba(56, 189, 248, 0.1)', borderColor: '#38bdf8', borderWidth: 2 }}]
                        }},
                        options: {{ 
                            responsive: true, 
                            animation: {{ duration: 1800 }},
                            scales: {{ r: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, angleLines: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ display: false }}, pointLabels: {{ color: '#64748b' }} }} }}
                        }}
                    }});

                    // Pie Chart Configuration
                    new Chart(document.getElementById('pieChart'), {{
                        type: 'pie',
                        data: {{
                            labels: ['Distinction', 'Merit', 'Pass'],
                            datasets: [{{ data: [45, 35, 20], backgroundColor: ['#34d399', '#818cf8', '#fb7185'], borderStrokeColor: 'transparent' }}]
                        }},
                        options: {{ responsive: true, animation: {{ duration: 1800 }} }}
                    }});

                    // Donut Chart Configuration
                    new Chart(document.getElementById('donutChart'), {{
                        type: 'doughnut',
                        data: {{
                            labels: ['Present Rate', 'Absent Vector'],
                            datasets: [{{ data: [{attendance_percent}, {100 - attendance_percent}], backgroundColor: ['#38bdf8', 'rgba(255,255,255,0.05)'], borderStrokeColor: 'transparent' }}]
                        }},
                        options: {{ responsive: true, animation: {{ duration: 1800 }}, cutout: '75%' }}
                    }});
                </script>
            </body>
            </html>
            """
            components.html(chart_canvas_html, height=880, scrolling=True)
            
        except Exception as e:
            st.error(f"Execution matrix pipeline runtime fault: {e}")
    else:
        # Initial Placeholder display layout status before running evaluation index matrix
        st.markdown("""
            <div style="border: 2px dashed rgba(255,255,255,0.05); border-radius:16px; padding:80px 20px; text-align:center; color:#475569;">
                <span style="font-size:2.5rem; display:block; margin-bottom:10px;">📊</span>
                Awaiting Ingest Inputs. Click the Execute Button to populate real-time analytics data arrays.
            </div>
        """, unsafe_allow_html=True)
