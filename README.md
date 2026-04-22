# 🌦️ Weather Classification App

A machine learning web application that predicts weather conditions based on
atmospheric inputs using a Decision Tree classifier.

---

## 📌 Project Overview

This project uses supervised machine learning to classify weather conditions
such as [Sunny / Rainy / Cloudy / Snowy] based on real-world meteorological
features. The model is deployed as an interactive web app using Streamlit.

---

## 🚀 Live Demo

> Run locally using the steps below.

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | Decision Tree Classifier |
| Test Accuracy | [X]% |
| Encoding | One-Hot Encoding for Location |
| Library | Scikit-learn |

---

## 📊 Features Used

| Feature | Type |
|---|---|
| Temperature | Numerical |
| Humidity | Numerical |
| Wind Speed | Numerical |
| Precipitation (%) | Numerical |
| Atmospheric Pressure | Numerical |
| UV Index | Numerical |
| Visibility (km) | Numerical |
| Location | Categorical (One-Hot Encoded) |

---

## 🗂️ Project Structure
weather-classification-app/
│
├── app.py                        # Streamlit web app
├── model/                        # Saved trained model (.pkl)
├── weather_classification_data.ipynb   # EDA + model training notebook
├── weather_classification_data.xlsx    # Dataset
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/saim-ansari-tech/weather-classification-app.git
cd weather-classification-app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📁 Dataset

- Source: [Dataset name / Weather Classification data]
- Records: 13200 rows
- Target Classes: [Sunny, Rainy, Cloudy, Snowy]

---

## 📈 Results

- **Test Accuracy:** 93%
- **Evaluation:** Classification Report generated in notebook

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Streamlit
- Pandas
- NumPy
- Joblib

---

## 👤 Author

**Saim** — Robotics & Intelligent Systems Student  
Bahria University Islamabad  
Aspiring AI/ML Engineer

---