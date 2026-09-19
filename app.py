import streamlit as st
import pandas as pd
import joblib
import time
import random

st.set_page_config(page_title="IBM Z Datathon: Real-Time Fraud Detector", layout="wide")
st.title("⚡ Real-Time E-Commerce Fraud Interceptor")
st.write("Simulating live transaction streams and making critical security decisions instantly.")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("fraud_model.pkl")

model = load_model()

# Load the simulation data
stream_data = pd.read_csv("simulation_stream.csv")

# Create placeholders for metrics
col1, col2, col3 = st.columns(3)
total_metric = col1.metric("Total Transactions Processed", 0)
safe_metric = col2.metric("Safe Transactions", 0)
fraud_metric = col3.metric("🚨 Fraud Alerts Triggered", 0)

# Create a placeholder for the live table
st.subheader("Live Transaction Stream Analysis")
table_placeholder = st.empty()

# Initialize session states to track counts
if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.safe = 0
    st.session_state.fraud = 0
    st.session_state.rows = []

# Start Simulation Button
if st.button("Start Live Stream Simulation"):
    for idx, row in stream_data.iterrows():
        # Format row for prediction
        current_tx = pd.DataFrame([row])
        
        # Make instant real-time prediction
        prediction = model.predict(current_tx)[0]
        
        # Generate clean details for display
        tx_amount = round(random.uniform(5.00, 2500.00), 2)
        status = "❌ FRAUD DETECTED" if prediction == 1 else "✅ SAFE"
        
        # Update counts
        st.session_state.total += 1
        if prediction == 1:
            st.session_state.fraud += 1
        else:
            st.session_state.safe += 1
            
        # Update metrics dynamically
        total_metric.metric("Total Transactions Processed", st.session_state.total)
        safe_metric.metric("Safe Transactions", st.session_state.safe)
        fraud_metric.metric("🚨 Fraud Alerts Triggered", st.session_state.fraud)
        
        # Append latest transaction to the top of our display list
        st.session_state.rows.insert(0, {
            "Transaction ID": f"TX_{1000 + idx}",
            "Simulated Amount ($)": tx_amount,
            "AI System Decision": status
        })
        
        # Display the live updating table
        table_placeholder.dataframe(pd.DataFrame(st.session_state.rows).head(10), use_container_width=True)
        
        # Controls the speed of the "real-time" stream
        time.sleep(0.6)