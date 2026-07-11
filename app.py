import streamlit as st
import pandas as pd
import joblib
model=joblib.load('knn_model.pkl')
scaler=joblib.load('scaler.pkl')
expected_columns=joblib.load('columns.pkl')
st.title("Heart Disease Prediction By Ayushmaan Gupta❤️")
st.markdown("Provide the following details to predict the risk of heart disease:")

age = st.slider("Age", 18, 100, 40)

sex = st.selectbox("SEX", ["M", "F"])

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    80, 200, 120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dL)",
    100, 600, 200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Max Heart Rate",
    60, 220, 150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    0.0, 6.0, 1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)


if st.button("Predict"):
    raw_input={
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        'Sex_'+sex: 1,
        'ChestPainType_'+chest_pain: 1,
        'RestingECG_'+resting_ecg: 1,
        'ExerciseAngina_'+exercise_angina: 1,
        'ST_Slope_'+st_slope: 1
    }
    input_data=pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0
    
    input_data = input_data[expected_columns]
    
    scaled_input_data = scaler.transform(input_data)  

    #No. [0] is not a default value. It is an index used to access the first element of a list (or NumPy array). 
    
    prediction=model.predict(scaled_input_data)[0]
    if (prediction==1):
        st.error("High risk of heart disease🫀🛑")
    else:
        st.success("Low risk of heart disease🫀✅")
    
    