import matplotlib.pyplot as plt


def class_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    df["Outcome"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Diabetes Class Distribution")
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Patients")

    return fig



def histograms(df):

    axes = df.hist(
        figsize=(12, 8),
        grid=False
    )

    fig = axes[0, 0].figure

    fig.suptitle("Feature Distributions", fontsize=16)

    plt.tight_layout()

    return fig



def correlation_heatmap(df):

    corr = df.corr()

    fig, ax = plt.subplots(figsize=(8,8))

    heatmap = ax.imshow(corr)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(heatmap)

    ax.set_title("Correlation Heatmap")

    return fig



def performance_chart(results):

    fig, ax = plt.subplots(figsize=(10,6))

    results.set_index("Model").plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylim(0,1)

    ax.set_ylabel("Score")

    ax.set_title("Model Performance Comparison")

    return fig