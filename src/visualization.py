"""Visualization functions for student performance analysis."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_relationship(df, x_column, x_label, title):
    """Create a scatter plot between an academic factor and final marks."""

    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_column], df["Final_Marks"])

    plt.xlabel(x_label)
    plt.ylabel("Final Marks")
    plt.title(title)

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_study_hours_vs_marks(df):
    """Plot study hours against final marks."""

    plot_relationship(
        df,
        "Study_Hours",
        "Study Hours",
        "Study Hours vs Final Marks"
    )


def plot_attendance_vs_marks(df):
    """Plot attendance against final marks."""

    plot_relationship(
        df,
        "Attendance",
        "Attendance (%)",
        "Attendance vs Final Marks"
    )


def plot_assignment_vs_marks(df):
    """Plot assignment score against final marks."""

    plot_relationship(
        df,
        "Assignment_Score",
        "Assignment Score",
        "Assignment Score vs Final Marks"
    )


def plot_performance_categories(df):
    """Create a bar chart showing the number of students in each category."""

    category_counts = df["Performance_Category"].value_counts()

    plt.figure(figsize=(8, 5))
    category_counts.plot(kind="bar")

    plt.xlabel("Performance Category")
    plt.ylabel("Number of Students")
    plt.title("Student Performance Categories")

    plt.xticks(rotation=0)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()


def plot_final_marks_distribution(df):
    """Show the number of students in different final-mark ranges."""

    bins = [0, 40, 60, 80, 101]
    labels = ["0–39", "40–59", "60–79", "80–100"]

    mark_ranges = pd.cut(
        df["Final_Marks"],
        bins=bins,
        labels=labels,
        right=False
    )

    range_counts = mark_ranges.value_counts().reindex(
        labels,
        fill_value=0
    )

    plt.figure(figsize=(8, 5))
    range_counts.plot(kind="bar")

    plt.xlabel("Final Marks Range")
    plt.ylabel("Number of Students")
    plt.title("Final Marks Distribution")

    plt.xticks(rotation=0)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()


def create_all_visualizations(df):
    """Generate all student performance visualizations."""

    plot_study_hours_vs_marks(df)
    plot_attendance_vs_marks(df)
    plot_assignment_vs_marks(df)
    plot_performance_categories(df)
    plot_final_marks_distribution(df)