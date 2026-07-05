import streamlit as st

from utils.data import load_data


def show_dataset():

    df = load_data()

    st.title("Dataset")

    st.markdown("""
    This page displays the Dataset used for training and evaluating the machine learning models.
    """)

    st.divider()

    # Dataset overview
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.divider()

    # Dataset preview
    st.subheader("Dataset Preview")

    st.dataframe(df, use_container_width=True)

    st.divider()

    # Column Information
    st.subheader("Column Information")

    info = {
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    }

    st.dataframe(info, use_container_width=True)

    st.divider()

    # Summary statistics
    st.subheader("Summary Statistics")

    st.dataframe(df.describe(), use_container_width=True)

    st.divider()

    # Missing values
    st.subheader("Missing Values")

    missing = df.isnull().sum().reset_index()

    missing.columns = [
        "Column",
        "Missing Values"
    ]

    st.dataframe(missing, use_container_width=True)

    if missing["Missing Values"].sum() == 0:
        st.success("No missing values found in the dataset.")