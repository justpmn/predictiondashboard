import streamlit as st

# Import pages
from views.home import show_home
from views.dataset import show_dataset
from views.visualizations import show_visualizations
from views.prediction import show_prediction
from views.performance import show_performance
from views.about import show_about

# page configuration
st.set_page_config(
    page_title="Diabetes Prediction Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


# sidebar nav
st.sidebar.title("Dashboard")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Dataset",
        "Visualizations",
        "Prediction",
        "Model Performance",
        "About"
    ]
)


# Route pages
if page == "Home":
    show_home()

elif page == "Dataset":
    show_dataset()

elif page == "Visualizations":
    show_visualizations()

elif page == "Prediction":
    show_prediction()

elif page == "Model Performance":
    show_performance()

elif page == "About":
    show_about()