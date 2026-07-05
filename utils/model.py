import streamlit as st
import joblib


@st.cache_resource
def load_model():

    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")

    return model, scaler