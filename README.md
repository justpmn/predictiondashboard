# Diabetes Prediction Dashboard

An interactive Machine Learning dashboard built with **Streamlit** that predicts whether a patient is likely to have diabetes using clinical measurements from the Pima Indians Diabetes Dataset.

---

## Project Overview

This project demonstrates an end-to-end Machine Learning workflow, including:

- Data exploration and preprocessing
- Data visualization
- Model training and evaluation
- Interactive prediction using a trained machine learning model
- Deployment using Streamlit Community Cloud

The application allows users to enter patient information and receive a diabetes prediction in real time.

---

## Dataset

The project uses the **Pima Indians Diabetes Dataset**, which contains diagnostic measurements for female patients of Pima Indian heritage.

### Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target Variable

- **Outcome**
  - 0 → Non-Diabetic
  - 1 → Diabetic

---

## Data Preprocessing

The dataset contained no explicit missing (`NaN`) values.

However, medically impossible zero values were identified in the following features:

- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI

These values were:

1. Replaced with `NaN`
2. Imputed using the **median**
3. Standardized using **StandardScaler**

---

## Machine Learning Models

The following classification algorithms were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

After evaluation, **Logistic Regression** achieved the best overall performance and was selected for deployment.

---

## Model Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Dashboard Features

The Streamlit dashboard includes:

-  Home Page
- Dataset Overview
- Data Visualizations
- Diabetes Prediction
-  Model Performance Comparison
-  About Page

---

##  Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

## Project Structure

```text
DiabetesDashboard/
│
├── app.py
├── requirements.txt
├── diabetes.csv
├── diabetes_model.pkl
├── scaler.pkl
│
├── utils/
│   ├── charts.py
│   ├── data.py
│   ├── metrics.py
│   └── model.py
│
├── views/
│   ├── home.py
│   ├── dataset.py
│   ├── visualizations.py
│   ├── prediction.py
│   ├── performance.py
│   └── about.py
│
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/justpmn/predictiondashboard.git
```

### 2. Navigate to the project directory

```bash
cd predictiondashboard
```

### 3. Create a virtual environment (Recommended)

#### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 4. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```
---

## Live Demo

Streamlit Dashboard: https://predictiondashboard-zdsa6fncpy9zhkikhzpzy9.streamlit.app/

## Screenshots

- Home Page
 <img width="950" height="400" alt="image" src="https://github.com/user-attachments/assets/84fcdce0-6b0e-4962-a80f-feae9f100a21" />

- Prediction Page
<img width="950" height="405" alt="image" src="https://github.com/user-attachments/assets/f6ba682a-9da8-4e82-aa7b-b9471193ec75" />

- Model Performance
<img width="950" height="401" alt="image" src="https://github.com/user-attachments/assets/523190eb-c0bf-4476-b9fc-17c1e1197bf6" />

- Visualizations
<img width="950" height="399" alt="image" src="https://github.com/user-attachments/assets/68aa2fa1-df33-436c-8e81-593b2e14fc1b" />

- Dataset
<img width="950" height="406" alt="image" src="https://github.com/user-attachments/assets/e5f59ae2-4a8b-4c0a-81e1-6c98cddf7282" />

- About
<img width="947" height="398" alt="image" src="https://github.com/user-attachments/assets/a436af0e-29e1-44d2-be23-927a00eddf58" />

---
