import streamlit as st
import pandas as pd

from utils.model import load_model


def show_prediction():

    model, scaler = load_model()

    st.title("Diabetes Prediction")

    st.markdown("""
    Enter the patient's medical information below to predict
    whether they are likely to have diabetes.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=2
        )

        glucose = st.number_input(
            "Glucose",
            min_value=0,
            max_value=300,
            value=120
        )

        blood_pressure = st.number_input(
            "Blood Pressure",
            min_value=0,
            max_value=200,
            value=70
        )

        skin_thickness = st.number_input(
            "Skin Thickness",
            min_value=0,
            max_value=100,
            value=20
        )

    with col2:

        insulin = st.number_input(
            "Insulin",
            min_value=0,
            max_value=900,
            value=80
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=25.5
        )

        pedigree = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.35
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=35
        )

    st.divider()

    if st.button("Predict Diabetes", use_container_width=True):

        patient = pd.DataFrame({

            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [pedigree],
            "Age": [age]

        })

        patient_scaled = scaler.transform(patient)

        prediction = model.predict(patient_scaled)[0]

        probability = model.predict_proba(patient_scaled)[0]

        confidence = max(probability) * 100

        st.subheader("Prediction Result")

        if prediction == 1:

            st.error(
                f"⚠️ Patient is likely diabetic.\n\nConfidence: {confidence:.2f}%"
            )

        else:

            st.success(
                f"✅ Patient is likely non-diabetic.\n\nConfidence: {confidence:.2f}%"
            )

        st.divider()

        st.subheader("Patient Information")

        st.dataframe(
            patient,
            use_container_width=True
        )