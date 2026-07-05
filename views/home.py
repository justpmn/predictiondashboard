import streamlit as st

from utils.metrics import (
    get_summary_metrics,
    get_best_model
)


def show_home():

    summary = get_summary_metrics()
    best = get_best_model()

    st.title(" Diabetes Prediction Dashboard")

    st.markdown("""
    Welcome to the **Diabetes Prediction Dashboard**.

    This application uses Machine Learning to predict whether a patient
    is likely to have diabetes based on diagnostic medical measurements.
    """)

    st.divider()

    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Patients",
        summary["Patients"]
    )

    col2.metric(
        "Features",
        summary["Features"]
    )

    col3.metric(
        "Models Tested",
        summary["Models"]
    )

    col4.metric(
        "Best Accuracy",
        summary["Best Accuracy"]
    )

    st.divider()

    # Best Model
    st.subheader(" Best Performing Model")

    st.success(
        f"""
        **{best['Model']}**

        Accuracy: **{best['Accuracy']:.2%}**

        Precision: **{best['Precision']:.2%}**

        Recall: **{best['Recall']:.2%}**

        F1 Score: **{best['F1 Score']:.2%}**
        """
    )

    st.divider()

    
    # Project Objective
    st.subheader("Project Objective")

    st.write("""
    The objective of this project is to develop a machine learning model
    capable of predicting diabetes using patient health information.

    Four classification algorithms were evaluated:

    - Logistic Regression
    - Decision Tree
    - Random Forest
    - Support Vector Machine (SVM)

    Their performances were compared using:

    - Accuracy
    - Precision
    - Recall
    - F1 Score
    """)

    st.divider()

    #Tech stach
    st.subheader("🛠 Tech Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.info("""
        **Programming**

        • Python

        • Streamlit
        """)

    with tech2:
        st.info("""
        **Machine Learning**

        • Scikit-Learn

        • Joblib
        """)

    with tech3:
        st.info("""
        **Data Analysis**

        • Pandas

        • NumPy

        • Matplotlib
        """)

    st.divider()

    st.caption(
        "Developed for the Machine Learning Group 2 Project."
    )