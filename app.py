import streamlit as st
import pickle
import numpy as np
import streamlit.components.v1 as components

# Set up page configuration
st.set_page_config(
    page_title="The Performance Ledger",
    page_icon="🎨",
    layout="centered"
)

# --- Handmade Premium Gallery & Celebration Animations (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f3ed;
        color: #3d2621;
        font-family: 'Quicksand', system-ui, sans-serif;
    }
    
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

    .gallery-card {
        background: #ffffff;
        border: 1px solid #e3dcd3;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 12px 24px -10px rgba(114, 28, 36, 0.12);
        position: relative;
    }
    
    .gallery-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: #d4af37; /* Gold Trim */
        border-radius: 16px 16px 0 0;
    }
    
    .gallery-card h3 {
        color: #721c24 !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 20px !important;
    }

    label {
        color: #5c4541 !important;
        font-weight: 600 !important;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #721c24 0%, #a93226 100%) !important;
        color: #ffffff !important;
        border: 1px solid #5c1218 !important;
        padding: 14px 28px !important;
        border-radius: 30px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px rgba(114, 28, 36, 0.25) !important;
    }

    .celebration-output {
        background: #fffdfa;
        border: 2px dashed #721c24;
        border-radius: 20px;
        padding: 40px;
        margin-top: 35px;
        text-align: center;
    }
    
    .output-score {
        font-size: 4.2rem !important;
        font-weight: 800 !important;
        color: #b8860b !important;
        font-family: 'Playfair Display', Georgia, serif;
        margin: 10px 0 15px 0;
    }

    .festive-row {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 25px;
        margin-top: 25px;
        height: 70px;
    }

    .candle { width: 14px; height: 45px; background: linear-gradient(to bottom, #d4af37, #721c24); border-radius: 3px 3px 0 0; position: relative; }
    .flame { width: 10px; height: 18px; background: radial-gradient(circle at bottom, #ffee55, #f39c12); border-radius: 50% 50% 20% 20%; position: absolute; top: -16px; left: 2px; animation: sway 0.5s infinite alternate ease-in-out; }
    .firecracker { width: 8px; height: 24px; background: #c0392b; border-top: 3px solid #f1c40f; position: relative; }
    .spark { position: absolute; top: -12px; left: -6px; width: 20px; height: 20px; background: radial-gradient(circle, #fff 10%, #ffeb3b 40%, transparent 70%); border-radius: 50%; animation: burst 0.4s infinite alternate ease-in-out; }

    .festive-row div:nth-child(even) .flame { animation-delay: 0.15s; }
    .festive-row div:nth-child(3) .spark { animation-delay: 0.2s; }

    @keyframes sway { 0% { transform: scale(1) rotate(-2deg); } 100% { transform: scale(1.15) rotate(2deg); filter: drop-shadow(0 0 8px #f39c12); } }
    @keyframes burst { 0% { transform: scale(0.6); opacity: 0.7; } 100% { transform: scale(1.4); opacity: 1; filter: drop-shadow(0 0 6px #ffeb3b); } }
    </style>
""", unsafe_allow_html=True)

# Load the model safely
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

# --- Title ---
st.markdown("<h1 class='gallery-title'>📜 The Learning Ledger</h1>", unsafe_allow_html=True)
st.markdown("<p class='gallery-tagline'>A classic artisanal workspace mapping predictive academic milestones.</p>", unsafe_allow_html=True)

# --- Inputs ---
st.markdown('<div class="gallery-card"><h3>📖 Behavioral Profiling</h3>', unsafe_allow_html=True)
hours_studied = st.number_input("📚 Weekly Study Duration (Hours)", min_value=0.0, max_value=168.0, value=10.0, step=0.5)
sleep_hours = st.number_input("😴 Daily Sleep Allocation (Hours/Night)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="gallery-card"><h3>📊 Performance Vectors</h3>', unsafe_allow_html=True)
attendance_percent = st.slider("🏫 Classroom Attendance Ratio (%)", min_value=0.0, max_value=100.0, value=85.0, step=1.0)
previous_scores = st.number_input("🥇 Prior Exam Baseline Score", min_value=0.0, max_value=100.0, value=70.0, step=1.0)
st.markdown('</div>', unsafe_allow_html=True)

# --- Trigger Optimization ---
if st.button("✨ Run Matrix Evaluation", use_container_width=True):
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])[cite: 1]
    
    try:
        prediction = model.predict(features)[0][cite: 1]
        
        # 1. Output Scoring & Firecracker Effects
        st.markdown(f"""
            <div class="celebration-output">
                <span style="color: #721c24; font-weight: 700; font-size: 0.95rem; display:block; margin-bottom: 5px; letter-spacing: 0.1em;">✨ EVALUATION VERIFIED SUCCESSFUL ✨</span>
                <span style="color: #8c7672; font-size: 1.1rem;">Projected Evaluation Index</span>
                <h1 class="output-score">{prediction:.2f}</h1>
                <div class="festive-row">
                    <div class="firecracker"><div class="spark"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="firecracker"><div class="spark"></div></div>
                    <div class="candle"><div class="flame"></div></div>
                    <div class="firecracker"><div class="spark"></div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. Animated Chart Suite Embedded Canvas
        st.markdown("<br><h3 style='text-align:center; color:#721c24; font-family:Georgia;'>📈 Live Performance Analytics Index</h3>", unsafe_allow_html=True)
        
        chart_html = f"""
        <html>
        <head>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {{ background-color: #faf8f5; font-family: sans-serif; padding: 10px; }}
                .chart-box {{ background: white; border: 1px solid #e3dcd3; border-radius: 12px; padding: 20px; margin-bottom: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); }}
                h4 {{ margin-top: 0; color: #721c24; text-align: center; border-bottom: 1px dashed #e3dcd3; padding-bottom: 8px; }}
                .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
                @media(max-width: 600px) {{ .grid-2 {{ grid-template-columns: 1fr; }} }}
            </style>
        </head>
        <body>
            <!-- Line Chart (Full Width) -->
            <div class="chart-box">
                <h4>📈 Monthly Marks Trend</h4>
                <canvas id="lineChart" height="120"></canvas>
            </div>

            <div class="grid-2">
                <!-- Bar Chart -->
                <div class="chart-box">
                    <h4>📊 Subject-wise Scores</h4>
                    <canvas id="barChart"></canvas>
                </div>
                <!-- Radar Chart -->
                <div class="chart-box">
                    <h4>🕸️ Skill Analysis</h4>
                    <canvas id="radarChart"></canvas>
                </div>
            </div>

            <div class="grid-2">
                <!-- Pie Chart -->
                <div class="chart-box">
                    <h4>🍕 Grade Distribution</h4>
                    <canvas id="pieChart"></canvas>
                </div>
                <!-- Donut Chart -->
                <div class="chart-box">
                    <h4>🍩 Attendance Matrix</h4>
                    <canvas id="donutChart"></canvas>
                </div>
            </div>

            <script>
                const options = {{
                    responsive: true,
                    animation: {{ duration: 2000, easing: 'easeOutQuart' }},
                    plugins: {{ legend: {{ labels: {{ color: '#5c4541' }} }} }}
                }};
                
                // Colors matched to Burgundy & Gold Theme
                const colors = ['#721c24', '#d4af37', '#a93226', '#e8c595', '#5c4541'];

                // 1. Line Chart
                new Chart(document.getElementById('lineChart'), {{
                    type: 'line',
                    data: {{
                        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                        datasets: [{{ label: 'Performance Progress', data: [65, 72, 68, 79, 83, {prediction}], borderColor: '#721c24', tension: 0.3, fill: false }}]
                    }},
                    options: options
                }});

                // 2. Bar Chart
                new Chart(document.getElementById('barChart'), {{
                    type: 'bar',
                    data: {{
                        labels: ['Math', 'Science', 'English', 'History'],
                        datasets: [{{ label: 'Score', data: [{previous_scores}, 82, 88, 74], backgroundColor: colors }}]
                    }},
                    options: options
                }});

                // 3. Radar Chart
                new Chart(document.getElementById('radarChart'), {{
                    type: 'radar',
                    data: {{
                        labels: ['Logic', 'Retention', 'Focus', 'Consistency', 'Participation'],
                        datasets: [{{ label: 'Current Standing', data: [80, 75, {hours_studied * 8}, {attendance_percent}, 85], backgroundColor: 'rgba(212, 175, 55, 0.2)', borderColor: '#d4af37' }}]
                    }},
                    options: options
                }});

                // 4. Pie Chart
                new Chart(document.getElementById('pieChart'), {{
                    type: 'pie',
                    data: {{
                        labels: ['Grade A', 'Grade B', 'Grade C'],
                        datasets: [{{ data: [40, 35, 25], backgroundColor: colors.slice(0,3) }}]
                    }},
                    options: options
                }});

                // 5. Donut Chart
                new Chart(document.getElementById('donutChart'), {{
                    type: 'doughnut',
                    data: {{
                        labels: ['Present (%)', 'Absent (%)'],
                        datasets: [{{ data: [{attendance_percent}, {100 - attendance_percent}], backgroundColor: ['#721c24', '#e3dcd3'] }}]
                    }},
                    options: options
                }});
            </script>
        </body>
        </html>
        """
        components.html(chart_html, height=900, scrolling=True)

    except Exception as e:
        st.error(f"Something went wrong with the entry evaluation: {e}")
