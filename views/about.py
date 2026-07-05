import streamlit as st


def show_about():

    st.title("About")

    st.markdown("""
    ## Diabetes Prediction Dashboard

    This project demonstrates how Machine Learning
    can assist in predicting diabetes using patient
    medical information.

    ### Dataset

    Pima Indians Diabetes Dataset

    ### Machine Learning Models

    - Logistic Regression
    - Decision Tree
    - Random Forest
    - Support Vector Machine (SVM)

    ### Evaluation Metrics

    - Accuracy
    - Precision
    - Recall
    - F1 Score

    ### Tech Stack

    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Scikit-Learn
    - Matplotlib

    ---
    Developed as part of the Machine Learning Group Project.
    Members: Peter Nyamu, Kimberly Wangari, Jesse Mbugua, Joe Ndeto and Joy Cherutich.
    """)