# Diabetes Prediction Using Machine Learning

## 📌 Project Overview
This project implements a **Diabetes Prediction System** using **Logistic Regression**. It allows users to input their health parameters and predict the likelihood of diabetes. The model is trained on a dataset from Kaggle and deployed using **Streamlit**.

## 🚀 Features
- Predicts whether a person is diabetic based on input parameters.
- Uses **Logistic Regression** for classification.
- Implements **Feature Scaling** for better accuracy.
- **User-friendly UI** built with Streamlit.
- Deployable via GitHub and Streamlit Cloud.

## 📂 Project Structure
```
Diabetes_Prediction_ML/
│-- main.ipynb         # Jupyter Notebook (Raw Data Preprocessing & Training)
│-- clean.ipynb        # Jupyter Notebook (Cleaned Data & Model Training)
│-- app.py             # Streamlit Web App
│-- final_model.pkl    # Trained Model
│-- scaler.pkl         # Scaler for Feature Scaling
│-- data/
│   │-- diabetes.csv   # Raw Dataset
│   │-- cleaned_data.csv  # Cleaned Dataset
│-- README.md          # Project Documentation
```

## 📥 Installation & Setup
### 🔹 Prerequisites
Ensure you have Python installed. You also need the following Python libraries:
```bash
pip install numpy pandas scikit-learn joblib streamlit
```

### 🔹 Clone Repository
```bash
git clone https://github.com/NewGenCoder25/Diabetes_Prediction_ML.git
cd Diabetes_Prediction_ML
```

### 🔹 Run the Web App
```bash
streamlit run app.py
```

## 📊 Model Training & Evaluation
- Used **Logistic Regression** for classification.
- Data preprocessing included **handling missing values** and **feature scaling**.
- The model achieved an accuracy of **XX%** on the test dataset.

## 📡 Deployment
The project can be deployed using **Streamlit Cloud** or **GitHub Pages**:
1. **Local Deployment:** Run `streamlit run app.py` in the terminal.
2. **Online Deployment:** Follow [Streamlit Cloud Deployment Guide](https://share.streamlit.io/).

## 📚 References
- [Kaggle Diabetes Dataset](https://www.kaggle.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---
### ✨ Developed by [Harsh Damame](https://github.com/NewGenCoder25)
