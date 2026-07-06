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
            "Random Forest (Tuned)",
            "Support Vector Machine"
        ],

        "Accuracy": [
            0.753,
            0.714,
            0.734,
            0.760,
            0.747
        ],

        "Precision": [
            0.667,
            0.596,
            0.625,
            0.661,
            0.667
        ],

        "Recall": [
            0.618,
            0.618,
            0.636,
            0.673,
            0.582
        ],

        "F1 Score": [
            0.642,
            0.607,
            0.631,
            0.667,
            0.621
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
        "Models": 5,
        "Best Model": best["Model"],
        "Best Accuracy": f"{best['Accuracy']*100:.2f}%"
    }