import streamlit as st
import pandas as pd
import joblib
import time

# Load Pipeline
pipeline = joblib.load("life_expectancy_pipeline.pkl")

# Page Configuration
st.set_page_config(
    page_title="Life Expectancy Predictor",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #E3F2FD, #E8F5E9);
    color: black !important;
}

p, h1, h2, h3, h4, h5, h6, label, div, span {
    color: black !important;
}

.main-title {
    text-align: center;
    color: #1565C0;
    font-size: 42px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #37474F;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<p class="main-title">🌍 Life Expectancy Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Predict Life Expectancy Using Socioeconomic Indicators</p>',
    unsafe_allow_html=True
)

# Project Info
st.info("""
📊 Machine Learning Regression Project

🔹 Model: Support Vector Regressor (SVR)

🔹 Target Variable: Life Expectancy Years

🔹 Features: HDI, GDP, Literacy, Poverty, Internet Access, Child Mortality and more
""")

st.subheader("📝 Enter Input Values")

# Inputs (Single Column)

hdi_score = st.slider(
    "HDI Score",
    0.0,
    1.0,
    0.75
)

urban_population_pct = st.slider(
    "Urban Population (%)",
    0,
    100,
    70
)

internet_penetration_pct = st.slider(
    "Internet Penetration (%)",
    0,
    100,
    75
)

social_protection_coverage_pct = st.slider(
    "Social Protection Coverage (%)",
    0,
    100,
    60
)

clean_water_access_pct = st.slider(
    "Clean Water Access (%)",
    0,
    100,
    90
)

electricity_access_pct = st.slider(
    "Electricity Access (%)",
    0,
    100,
    95
)

literacy_rate_pct = st.slider(
    "Literacy Rate (%)",
    0,
    100,
    85
)

gdp_per_capita_usd = st.number_input(
    "GDP Per Capita (USD)",
    min_value=0,
    value=10000
)

poverty_rate_pct = st.slider(
    "Poverty Rate (%)",
    0,
    100,
    20
)

child_mortality_per_1000 = st.slider(
    "Child Mortality per 1000",
    0,
    100,
    15
)

# Input DataFrame
input_data = pd.DataFrame({

    'hdi_score':[hdi_score],
    'urban_population_pct':[urban_population_pct],
    'internet_penetration_pct':[internet_penetration_pct],
    'social_protection_coverage_pct':[social_protection_coverage_pct],
    'clean_water_access_pct':[clean_water_access_pct],
    'electricity_access_pct':[electricity_access_pct],
    'literacy_rate_pct':[literacy_rate_pct],
    'gdp_per_capita_usd':[gdp_per_capita_usd],
    'poverty_rate_pct':[poverty_rate_pct],
    'child_mortality_per_1000':[child_mortality_per_1000]

})

# Prediction Button
if st.button("🚀 Predict Life Expectancy"):

    with st.spinner("Calculating Prediction..."):
        time.sleep(2)

        prediction = pipeline.predict(input_data)

    st.markdown("## 🎯 Prediction Result")

    st.metric(
        label="Predicted Life Expectancy",
        value=f"{prediction[0]:.2f} Years"
    )

    if prediction[0] >= 80:
        st.success("🌟 Excellent Life Expectancy")

    elif prediction[0] >= 70:
        st.info("✅ High Life Expectancy")

    elif prediction[0] >= 60:
        st.warning("⚠ Moderate Life Expectancy")

    else:
        st.error("❌ Low Life Expectancy")

# Input Summary
with st.expander("📋 View Input Summary"):

    st.dataframe(
        input_data,
        use_container_width=True
    )