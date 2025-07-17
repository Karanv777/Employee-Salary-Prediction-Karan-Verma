import streamlit as st
import joblib as jb
import pandas as pd

model = jb.load("salary_pipeline.pkl")

st.set_page_config(page_title="Salary Predictor")
st.title("Income Class Prediction App")
st.markdown("Predict an employee's salary based on input features.")

st.divider()

age = st.number_input("Age", min_value=18, max_value=70, value=30)

education = st.selectbox("Education Level", [
    "Bachelors", "Masters", "PhD", "Doctorate", "HS-grad", "Assoc", "Some-college"
])

occupation = st.selectbox("Occupation", 
                          ["Prof-specialty", "Craft-repair", "Exec-managerial", "Adm-clerical", "Sales", "Other-service", "Machine-op-inspct", "Transport-moving", "Handlers-cleaners", "Farming-fishing", "Tech-support", "Protective-serv", "Priv-house-serv", "Armed-Forces", "Others"
                          ]) 

workclass = st.selectbox("Organization", [
    "Private", "self-emp-not-inc", "Local-gov", "State-gov", "Self-emp-inc", "Federal-gov", "Others"
])

hours_per_week = st.slider("Work Hours per Week", 1, 80, 40)

st.divider()

input_df = pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'workclass': [workclass]
})

st.write("Input Data")
st.write(input_df)

if st.button("Predict Salary"):
    
    prediction = model.predict(input_df)[0]
    
    st.success(f"Predicted Income Class : **{prediction}**")