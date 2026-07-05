import streamlit as st

from utils.data import load_data
from utils.charts import (
    class_distribution,
    histograms,
    correlation_heatmap
)


def show_visualizations():

    df = load_data()

    st.title("import streamlit as st")

from utils.data import load_data
from utils.charts import (
    class_distribution,
    histograms,
    correlation_heatmap
)


def show_visualizations():

    df = load_data()

    st.title("Data Visualizations")

    st.markdown("""
    These visualizations help us understand the dataset
    before training machine learning models.
    """)

    st.divider()

    st.subheader("Class Distribution")

    st.pyplot(class_distribution(df))

    st.divider()

    st.subheader("Feature Distributions")

    st.pyplot(histograms(df))

    st.divider()

    st.subheader("Correlation Heatmap")

    st.pyplot(correlation_heatmap(df))

    