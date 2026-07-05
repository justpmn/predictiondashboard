import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    """
    Load the diabetes dataset.
    """

    df = pd.read_csv("diabetes.csv")

    return df