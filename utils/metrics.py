import pandas as pd


def get_model_metrics():
    """
    Returns the evaluation metrics for all trained models.
    """

    results = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "Support Vector Machine"
        ],

        "Accuracy": [
            0.753,
            0.747,
            0.721,
            0.734
        ],

        "Precision": [
            0.649,
            0.625,
            0.607,
            0.646
        ],

        "Recall": [
            0.673,
            0.727,
            0.618,
            0.564
        ],

        "F1 Score": [
            0.661,
            0.672,
            0.613,
            0.602
        ]
    })

    return results


def get_best_model():
    """
    Returns the best-performing model based on accuracy.
    """

    results = get_model_metrics()

    best = results.loc[results["Accuracy"].idxmax()]

    return best


def get_summary_metrics():
    """
    Returns the dashboard summary metrics.
    """

    best = get_best_model()

    return {
        "Patients": 768,
        "Features": 8,
        "Models": 4,
        "Best Model": best["Model"],
        "Best Accuracy": f"{best['Accuracy']*100:.2f}%"
    }