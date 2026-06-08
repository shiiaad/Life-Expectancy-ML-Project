import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="centered")

st.title("Customer Churn Prediction App")
st.write("Enter customer details below. The app sends raw inputs directly into the saved machine learning pipeline.")

@st.cache_resource
def load_model():
    return joblib.load("churn_pipeline.joblib")

pipeline = load_model()

with st.form("prediction_form"):
    credit_score = st.slider("Credit Score", 300, 900, 650)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.slider("Age", 18, 100, 40)
    tenure = st.slider("Tenure", 0, 10, 5)
    balance = st.number_input("Balance", min_value=0.0, value=60000.0, step=1000.0)
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    has_cr_card = st.selectbox("Has Credit Card", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    is_active_member = st.selectbox("Is Active Member", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0, step=1000.0)

    submitted = st.form_submit_button("Predict Churn")

if submitted:
    input_data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Geography": [geography],
        "Gender": [gender],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_products],
        "HasCrCard": [has_cr_card],
        "IsActiveMember": [is_active_member],
        "EstimatedSalary": [estimated_salary],
    })

    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"Customer is likely to churn. Churn probability: {probability:.2%}")
    else:
        st.success(f"Customer is not likely to churn. Churn probability: {probability:.2%}")

    st.write("Raw input sent to pipeline:")
    st.dataframe(input_data)
