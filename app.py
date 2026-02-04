import streamlit as st
import pandas as pd
import joblib

# Streamlit app title
st.title("CNC Machine Fault Prediction App")

# Load the trained model
model = joblib.load("cnc_fault_model.pkl")

# Add user input form for prediction
st.write("### Enter Machine Parameters")

# Create input fields for each feature
spindle_speed = st.number_input("Spindle Speed", min_value=0, value=5000)
vibration = st.number_input("Vibration", min_value=0.0, value=0.02, format="%.2f")
tool_temperature = st.number_input("Tool Temperature", min_value=0, value=75)
motor_current = st.number_input("Motor Current", min_value=0, value=10)
feed_rate = st.number_input("Feed Rate", min_value=0.0, value=0.5, format="%.2f")
tool_wear = st.number_input("Tool Wear", min_value=0.0, value=0.1, format="%.2f")

# Predict button
if st.button("Predict Fault"):
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        "spindle_speed": [spindle_speed],
        "vibration": [vibration],
        "tool_temperature": [tool_temperature],
        "motor_current": [motor_current],
        "feed_rate": [feed_rate],
        "tool_wear": [tool_wear]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction[0] == 0:
        st.success("The machine is operating normally.")
    else:
        # Example logic to determine the issue based on input values
        issue = "Unknown issue"
        if vibration > 0.04:
            issue = "High vibration detected"
        elif tool_temperature > 80:
            issue = "Tool overheating"
        elif motor_current > 12:
            issue = "Excessive motor current"
        elif tool_wear > 0.3:
            issue = "Tool wear exceeds limit"
        st.error(f"Fault detected in the machine! Issue: {issue}")