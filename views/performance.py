import streamlit as st

from utils.metrics import (
    get_model_metrics,
    get_best_model
)

from utils.charts import performance_chart


def show_performance():

    st.title("Model Performance")

    st.markdown("""
    This page compares the performance of all the machine learning
    models that were trained on the diabetes dataset.
    """)

    st.divider()

    
    # Load metrics
    results = get_model_metrics()
    best = get_best_model()

    
    #Best Model Card
    st.subheader("Best Performing Model")

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

    
    # Metric cards
    
    st.subheader("Best Scores")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Accuracy",
        f"{results['Accuracy'].max()*100:.2f}%"
    )

    col2.metric(
        "Precision",
        f"{results['Precision'].max()*100:.2f}%"
    )

    col3.metric(
        "Recall",
        f"{results['Recall'].max()*100:.2f}%"
    )

    col4.metric(
        "F1 Score",
        f"{results['F1 Score'].max()*100:.2f}%"
    )

    st.divider()

    
    # Performance Table
    
    st.subheader("Evaluation Metrics")

    st.dataframe(
        results,
        use_container_width=True
    )

    st.divider()

    
    # Performance Chart
    
    st.subheader("Model Comparison")

    fig = performance_chart(results)

    st.pyplot(fig)

    st.divider()

    
    # Conclusion
    
    st.subheader("Conclusion")

    st.info(
        f"""
        Among the four machine learning algorithms tested,
        **{best['Model']}** achieved the highest prediction accuracy
        of **{best['Accuracy']:.2%}** and was selected as the final
        model for deployment in this dashboard.
        """
    )