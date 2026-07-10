# ❤️ Heart Disease Risk Prediction Web Application

> **An End-to-End Machine Learning & Streamlit Application for Predicting Heart Disease Risk**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

# 📖 Overview

Heart disease remains one of the leading causes of death worldwide. Early prediction of cardiovascular risk can help individuals seek timely medical attention and support healthcare professionals in preliminary risk assessment.

This project implements a **complete Machine Learning pipeline** that predicts the likelihood of heart disease based on clinical parameters. The trained model is deployed through a **Streamlit web application**, allowing users to enter medical information and receive instant predictions.

The project demonstrates the entire workflow from **data preprocessing** to **model deployment**, making it an excellent portfolio project for Machine Learning and Data Science.

---

# ✨ Features

- ❤️ Heart Disease Risk Prediction
- 📊 Interactive Streamlit Dashboard
- 🤖 Machine Learning Classification
- 📈 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- ⚙️ Feature Scaling
- 🔄 One-Hot Encoding
- 📋 Multiple Model Comparison
- 💾 Model Serialization using Joblib
- ⚡ Real-Time Prediction

---

# 📂 Project Structure

```text
Heart-Disease-Risk-Prediction/
│
├── app.py
├── heart.py
├── heart.csv
├── knn_model.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The dataset contains patient medical information used for predicting heart disease.

## Features

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

### Target

```text
HeartDisease

0 → Low Risk

1 → High Risk
```

---

# 📈 Exploratory Data Analysis

The project performs comprehensive EDA including:

- Distribution Plots
- Count Plots
- Box Plots
- Violin Plots
- Correlation Heatmaps
- Class Distribution Analysis

---

# 🧹 Data Preprocessing

The preprocessing pipeline includes:

- Duplicate Checking
- Invalid Value Handling
- Mean Imputation for Incorrect Values
- One-Hot Encoding
- Feature Scaling using StandardScaler

---

# 🤖 Machine Learning Models

The following algorithms were trained and evaluated:

| Model | Description |
|--------|-------------|
| Logistic Regression | Linear Classification |
| Gaussian Naive Bayes | Probabilistic Classifier |
| Decision Tree | Tree-Based Model |
| Support Vector Machine | Margin-Based Classifier |
| K-Nearest Neighbors | Distance-Based Classifier |

After evaluation, **K-Nearest Neighbors (KNN)** was selected as the deployment model.

---

# 📊 Evaluation Metrics

The models are compared using:

- Accuracy Score
- F1 Score
- Classification Report

This helps identify the most suitable model for deployment.

---

# 🌐 Streamlit Application

The web application allows users to enter patient details and receive a prediction in real time.

### User Inputs

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

### Prediction Output

🟢 Low Risk of Heart Disease

🔴 High Risk of Heart Disease

---

# 🛠 Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Heart-Disease-Risk-Prediction.git
```

Move into the project

```bash
cd Heart-Disease-Risk-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn joblib
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🔄 Workflow

```text
Heart Disease Dataset
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
One-Hot Encoding
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Model Comparison
        │
        ▼
KNN Model Selection
        │
        ▼
Model Serialization
        │
        ▼
Streamlit Web Application
        │
        ▼
Heart Disease Prediction
```

---

# 📚 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Visualization
- Feature Engineering
- One-Hot Encoding
- Feature Scaling
- Machine Learning Classification
- Model Evaluation
- Model Serialization
- Streamlit Deployment

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- ROC-AUC Comparison
- SHAP Explainability
- Docker Deployment
- Cloud Deployment (Streamlit Community Cloud / Render)
- User Authentication
- Prediction History

---

# 📜 Disclaimer

> This application is intended for educational purposes only and should not be used as a substitute for professional medical advice or diagnosis.

---

# 👨‍💻 Author

**Ayushmaan Gupta**

🎓 B.Tech CSE (Artificial Intelligence & Machine Learning)

**Interests**

- Artificial Intelligence
- Machine Learning
- Healthcare AI
- Data Science
- Computer Vision

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

<div align="center">

### ❤️ Built with Python, Machine Learning & Streamlit

*"Machine Learning can support healthcare by providing intelligent insights, but medical decisions should always be made by qualified professionals."*

</div>
