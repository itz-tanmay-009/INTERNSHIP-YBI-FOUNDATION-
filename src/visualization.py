"""Functions for visualizing student academic performance."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_scatter(df, x_column, y_column, title):
    """Create a scatter plot for two numerical columns."""

    plt.figure(figsize=(8, 5))
    plt.scatter(
        df[x_column],
        df[y_column],
        edgecolors="black"
    )

    plt.title(title)
    plt.xlabel(x_column.replace("_", " "))
    plt.ylabel(y_column.replace("_", " "))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_study_hours_vs_marks(df):
    """Show the relationship between study hours and final marks."""

    plot_scatter(
        df,
        "Study_Hours",
        "Final_Marks",
        "Study Hours vs Final Marks"
    )


def plot_attendance_vs_marks(df):
    """Show the relationship between attendance and final marks."""

    plot_scatter(
        df,
        "Attendance",
        "Final_Marks",
        "Attendance vs Final Marks"
    )


def plot_assignment_vs_marks(df):
    """Show the relationship between assignment scores and final marks."""

    plot_scatter(
        df,
        "Assignment_Score",
        "Final_Marks",
        "Assignment Score vs Final Marks"
    )


def plot_previous_vs_final_marks(df):
    """Show the relationship between previous and final marks."""

    plot_scatter(
        df,
        "Previous_Marks",
        "Final_Marks",
        "Previous Marks vs Final Marks"
    )


def plot_performance_categories(df):
    """Display the number of students in each performance category."""

    if "Performance_Category" not in df.columns:
        raise ValueError(
            "The dataset must contain Performance_Category."
        )

    category_counts = df["Performance_Category"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(
        category_counts.index,
        category_counts.values,
        edgecolor="black"
    )

    plt.title("Student Performance Categories")
    plt.xlabel("Performance Category")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=15)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_final_marks_distribution(df):
    """Display the distribution of final examination marks."""

    if "Final_Marks" not in df.columns:
        raise ValueError("The dataset must contain Final_Marks.")

    bins = [0, 40, 60, 80, 101]
    labels = ["0–39", "40–59", "60–79", "80–100"]

    mark_groups = pd.cut(
        df["Final_Marks"],
        bins=bins,
        labels=labels,
        right=False
    )

    mark_counts = mark_groups.value_counts().reindex(
        labels,
        fill_value=0
    )

    plt.figure(figsize=(8, 5))
    plt.bar(
        mark_counts.index,
        mark_counts.values,
        edgecolor="black"
    )

    plt.title("Distribution of Final Marks")
    plt.xlabel("Marks Range")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_grade_distribution(df):
    """Display the distribution of students across performance grades."""

    if "Grade" not in df.columns:
        raise ValueError("The dataset must contain a Grade column.")

    grade_counts = df["Grade"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar(
        grade_counts.index,
        grade_counts.values,
        edgecolor="black"
    )

    plt.title("Student Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def create_all_visualizations(df):
    """Generate the main project visualizations."""

    plot_study_hours_vs_marks(df)
    plot_attendance_vs_marks(df)
    plot_assignment_vs_marks(df)
    plot_previous_vs_final_marks(df)
    plot_performance_categories(df)
    plot_final_marks_distribution(df)