# life-expectancy-prediction-ml
Machine Learning regression project that predicts life expectancy using socioeconomic indicators. Includes EDA, feature engineering, SVR model, automated pipeline integration, and Streamlit deployment.

## Life Expectancy Prediction Using Machine Learning
### Project Overview

This project predicts life expectancy years using socioeconomic and development indicators such as HDI score, literacy rate, poverty rate, internet penetration, GDP per capita, clean water access, and child mortality.

The project follows a complete Machine Learning workflow including:

### Problem Definition
- Data Collection & Ingestion
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Selection
- Model Training & Comparison
- Pipeline Integration
- Streamlit Deployment
 
### Problem Statement

Life expectancy is an important indicator of a country's overall development and quality of life. Governments and organizations can use predictive analytics to understand how socioeconomic factors influence life expectancy.

The objective of this project is to build a machine learning model that accurately predicts:

### Target Variable:
life_expectancy_years

### Dataset Information

Dataset Source : Kaggle

Domain : Global Poverty & Economic Inequality

Rows : 25

Columns : 10000

Problem Type : Regression

Target Variable : life_expectancy_years

### Exploratory Data Analysis (EDA)
The following analyses were performed:
- Statistical Summary
- Missing Value Analysis
- Distribution Analysis
- Outlier Detection
- Correlation Analysis
- Feature Relationship Analysis

### Visualizations
- Histogram
- Boxplot
- Correlation Heatmap
- HDI vs Life Expectancy
- Poverty Rate vs Life Expectancy
- Child Mortality vs Life Expectancy

Top Feature Importance Visualization


### Data Preprocessing
The following preprocessing techniques were applied:
- Missing Value Handling
 Mean Imputation
- Categorical Encoding
 Label Encoding
- Feature Scaling
 StandardScaler


### Feature Selection
Selected highly correlated features to improve model performance and reduce noise.

### Machine Learning Models
The following regression algorithms were trained and evaluated:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors Regressor (KNN)
- Support Vector Regressor (SVR)


### Model Evaluation Metrics
The models were evaluated using:
- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### Best Performing Model
Support Vector Regressor (SVR)
The SVR model achieved the best overall performance with the highest R² score and lowest prediction error.

Hyperparameter tuning was performed using GridSearchCV to optimize:
C

Kernel

Gamma



### Pipeline Integration
To prevent data leakage and automate preprocessing, an end-to-end Scikit-Learn Pipeline was created.
The pipeline includes:
- Missing Value Imputation
- Feature Scaling
- SVR Model

The complete pipeline was saved as:
life_expectancy_pipeline.pkl

### Streamlit Deployment
A Streamlit web application was developed for real-time predictions.
Users can:

Enter socioeconomic indicators

Submit inputs

Receive instant life expectancy predictions

#### Run Application
streamlit run app.py


### Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit


### Key Insights
- HDI score positively influences life expectancy.
- Literacy rate and internet access contribute to higher life expectancy.
- Poverty rate negatively impacts life expectancy.
- Child mortality has a strong negative relationship with life expectancy.
- Socioeconomic development indicators are strong predictors of life expectancy.

### Conclusion
This project successfully developed a machine learning model to predict life expectancy using socioeconomic indicators. After comparing multiple regression algorithms, SVR emerged as the best-performing model. The final solution was integrated into an automated pipeline and deployed using Streamlit, enabling real-time predictions through a user-friendly interface.

### Future Improvements

- Include additional healthcare indicators.
- Use more recent global datasets.
- Experiment with XGBoost and LightGBM.
- Deploy the application to Streamlit Cloud.
- Implement country-level comparative analytics.# Machine-Learning-Project
