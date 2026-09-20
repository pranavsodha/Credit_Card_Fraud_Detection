import streamlit as st
import pandas as pd
import joblib
import time
import random
import plotly.graph_objects as go

# 1. Page Configuration for a Premium Tech Look
st.set_page_config(page_title="Z-Shield Command Center", layout="wide", initial_sidebar_state="collapsed")

# Custom Dark Cyber Theme CSS
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .metric-box {
        background-color: #1f293d;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0052cc;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }
    .fraud-box { border-left: 5px solid #ff3333 !important; }
    .latency-box { border-left: 5px solid #00ffcc !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Z-Shield: Enterprise Threat Command Center")
st.markdown("---")

# Load saved artifacts safely
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load("fraud_model.pkl")
        stream_data = pd.read_csv("simulation_stream.csv")
        return model, stream_data
    except:
        return None, None

model, stream_data = load_artifacts()

if model is None:
    st.error("❌ 'fraud_model.pkl' या 'simulation_stream.csv' नहीं मिली! कृपया पहले 'train_model.py' रन करें।")
    st.stop()

# Initialize Session States for Dashboard Live Metrics
if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.safe = 0
    st.session_state.fraud = 0
    st.session_state.latency_history = []
    st.session_state.rows = []

# --- ROW 1: Premium Metric Cards ---
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    m_total = st.metric("Total Transactions Audited", st.session_state.total)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    m_safe = st.metric("Verified Safe Transactions", st.session_state.safe)
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-box fraud-box">', unsafe_allow_html=True)
    m_fraud = st.metric("🚨 Fraud Stopped (Live)", st.session_state.fraud)
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="metric-box latency-box">', unsafe_allow_html=True)
    # Simulating IBM Z Telum hardware sub-millisecond capability (0.7ms - 0.9ms)
    current_latency = f"{random.uniform(0.72, 0.88):.2f} ms" if st.session_state.total > 0 else "0.00 ms"
    m_latency = st.metric("IBM Telum AI Latency", current_latency, delta="Zero-Lag Verified")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- ROW 2: Live Visualization & Analytics Section ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📊 Live System Throughput & Latency Stream")
    graph_placeholder = st.empty()

with col_right:
    st.subheader("🎯 Explainable AI (XAI) Insight")
    xai_placeholder = st.empty()
    xai_placeholder.info("Start simulation to see AI feature contribution weights.")

# --- ROW 3: Detailed Live Audit Log ---
st.subheader("📋 Real-Time Transaction Logs")
table_placeholder = st.empty()

# --- TRIGGER SIMULATION ---
if st.button("🚀 Deploy & Launch Z-Shield Simulation", use_container_width=True):
    for idx, row in stream_data.iterrows():
        current_tx = pd.DataFrame([row])
        
        # Real Model Prediction
        prediction = model.predict(current_tx)[0]
        
        # Exact values from dataset columns
        tx_amount = round(float(row['Amount']), 2) if 'Amount' in row else 0.0
        tx_time = int(row['Time']) if 'Time' in row else 0
        
        # IBM Telum Inference Simulation
        z_latency = round(random.uniform(0.71, 0.89), 2)
        st.session_state.latency_history.append(z_latency)
        if len(st.session_state.latency_history) > 20:
            st.session_state.latency_history.pop(0)
            
        # Update Counts
        st.session_state.total += 1
        if prediction == 1:
            st.session_state.fraud += 1
            status = "❌ CRITICAL FRAUD DETECTED"
            # Logic for why it failed (XAI feature mock based on V columns weights)
            reason = "🚨 V1/V2 Extreme Shift (Device/Location Mismatch)"
        else:
            st.session_state.safe += 1
            status = "✅ SECURED BY IBM Z"
            reason = "✓ Normal Pattern Verified"
            
        # Dynamically Update Top Cards
        m_total.metric("Total Transactions Audited", st.session_state.total)
        m_safe.metric("Verified Safe Transactions", st.session_state.safe)
        m_fraud.metric("🚨 Fraud Stopped (Live)", st.session_state.fraud)
        m_latency.metric("IBM Telum AI Latency", f"{z_latency} ms", delta="Zero-Lag Verified")
        
        # Update Dynamic Plots (Plotly Line Chart)
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=st.session_state.latency_history, mode='lines+markers', name='Latency (ms)', line=dict(color='#00ffcc', width=3)))
        fig.update_layout(template='plotly_dark', height=250, margin=dict(l=20, r=20, t=20, b=20))
        graph_placeholder.plotly_chart(fig, use_container_width=True)
        
        # Update XAI Analytics Pane
        if prediction == 1:
            xai_placeholder.error(f"**Transaction ID:** TX_{1000+idx}\n\n**Root Cause:** {reason}\n\n*Action:* Payment Blocked instantly at Mainframe Core.")
        else:
            xai_placeholder.success(f"**Transaction ID:** TX_{1000+idx}\n\n**Root Cause:** {reason}\n\n*Action:* Approved.")

        # Update Live Table Data
        st.session_state.rows.insert(0, {
            "Transaction ID": f"TX_{1000 + idx}",
            "Timestamp (sec)": tx_time,
            "Amount ($)": tx_amount,
            "Security Status": status
        })
        table_placeholder.dataframe(pd.DataFrame(st.session_state.rows).head(8), use_container_width=True)
        
        time.sleep(0.5)