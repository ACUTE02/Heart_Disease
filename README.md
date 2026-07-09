# ❤️ Heart Disease Risk Prediction using Machine Learning

### End-to-End Machine Learning Pipeline with Future Streamlit Deployment

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

# 📖 Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help doctors and patients take preventive action.

This project builds an **end-to-end Machine Learning pipeline** to predict the risk of heart disease using patient medical data.

The project covers:

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning
- ⚙ Feature Engineering
- 🔄 Data Preprocessing
- 🤖 Multiple Machine Learning Models
- 📈 Performance Comparison
- 💾 Model Serialization using Joblib
- 🚀 Future Streamlit Deployment

---

# 🎯 Objectives

- Analyze heart disease data.
- Clean missing and inconsistent values.
- Engineer meaningful features.
- Compare multiple ML classification algorithms.
- Select the best-performing model.
- Save the trained model for deployment.
- Build a Streamlit web application (future work).

---

# 📂 Repository Structure

```text
Heart-Disease-Risk-Prediction/
│
├── heart.py
├── heart.csv
├── knn_model.pkl
├── scaler.pkl
├── columns.pkl
├── README.md
└── app.py              (Coming Soon)
```

---

# 📊 Dataset Features

The dataset contains patient health information such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- ECG Results
- Maximum Heart Rate
- Exercise Angina
- Oldpeak
- ST Slope

### Target

```text
HeartDisease

0 → No Heart Disease

1 → Heart Disease
```

---

# 📊 Exploratory Data Analysis

The project performs several visualization techniques:

✅ Distribution Plots

- Age
- Resting Blood Pressure
- Cholesterol
- Maximum Heart Rate

✅ Count Plots

- Gender
- Chest Pain Type
- Fasting Blood Sugar

✅ Box Plot

Cholesterol vs Heart Disease

✅ Violin Plot

Age Distribution

✅ Correlation Heatmap

Relationship between numerical features

---

# 🧹 Data Cleaning

The preprocessing pipeline includes:

### Missing Value Handling

Invalid values such as

```
RestingBP = 0

Cholesterol = 0
```

are replaced using the mean of valid observations.

---

### One-Hot Encoding

Categorical variables are converted into numerical features using:

```python
pd.get_dummies()
```

---

### Feature Scaling

Numerical features are standardized using:

```python
StandardScaler
```

---

# 🤖 Machine Learning Models

Five different classification algorithms are trained and compared.

| Model | Purpose |
|--------|----------|
| Logistic Regression | Baseline Model |
| Gaussian Naive Bayes | Probabilistic Classification |
| Decision Tree | Tree-Based Learning |
| Support Vector Machine (SVM) | Margin-Based Classification |
| K-Nearest Neighbors (KNN) | Distance-Based Classification |

---

# 📈 Model Evaluation

Each model is evaluated using:

- Accuracy Score
- F1 Score
- Classification Report

The best-performing model is selected for deployment.

---

# 💾 Model Serialization

The trained model is saved using Joblib.

Generated Files:

```text
knn_model.pkl

scaler.pkl

columns.pkl
```

These files are later used by the Streamlit application for making predictions.

---


# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib

---

# 📦 Python Libraries

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
joblib
```

---

# 🚀 Installation

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
pip install numpy pandas matplotlib seaborn scikit-learn joblib
```

Run the training script

```bash
python heart.py
```

---

# 🔄 Machine Learning Workflow

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
Feature Encoding
         │
         ▼
Feature Scaling
         │
         ▼
Train-Test Split
         │
         ▼
Train Multiple Models
         │
         ▼
Model Comparison
         │
         ▼
Save Best Model
         │
         ▼
Future Streamlit Deployment
```

---

# 📚 Concepts Covered

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- One-Hot Encoding
- Feature Scaling
- Machine Learning Classification
- Model Comparison
- Performance Evaluation
- Model Serialization
- Deployment Preparation

---

# 👨‍💻 Author

**Ayushmaan Gupta**

🎓 B.Tech CSE (AI & ML)

### Interests

- Artificial Intelligence
- Machine Learning
- Healthcare AI
- Computer Vision
- Data Science

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

> **⚠️ Disclaimer**
>
> This project is intended for educational and research purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment.

---

<div align="center">

**Made with ❤️ by Ayushmaan Gupta**

*"AI cannot replace doctors, but it can empower them with faster and smarter predictions."*

</div>
