
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output" / "charts"


def create_output_directory(output_dir=None):
    """Create the directory used to store charts."""
    if output_dir is None:
        output_dir = DEFAULT_OUTPUT_DIR

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _save_chart(fig, output_dir, filename):
    path = output_dir / filename
    try:
        fig.tight_layout()
        fig.savefig(path, dpi=150)
    finally:
        plt.close(fig)
    return path


def create_marks_comparison_chart(df, output_dir=None):
    """Compare average marks across assessment categories."""
    output_dir = create_output_directory(output_dir)

    columns = ["Previous_Marks", "Assignment_Marks", "Final_Marks"]
    averages = df[columns].mean()

    fig, ax = plt.subplots(figsize=(8, 5))
    averages.plot(kind="bar", ax=ax)

    ax.set_title("Average Marks Comparison")
    ax.set_xlabel("Assessment")
    ax.set_ylabel("Average Marks")
    ax.set_ylim(0, 100)
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    return _save_chart(fig, output_dir, "marks_comparison.png")


def create_study_hours_chart(df, output_dir=None):
    """Show study hours for each student."""
    output_dir = create_output_directory(output_dir)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df["Student_ID"], df["Study_Hours"])

    ax.set_title("Study Hours by Student")
    ax.set_xlabel("Student ID")
    ax.set_ylabel("Study Hours")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    return _save_chart(fig, output_dir, "study_hours.png")


def create_attendance_chart(df, output_dir=None):
    """Show attendance percentages for each student."""
    output_dir = create_output_directory(output_dir)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df["Student_ID"], df["Attendance"])

    ax.set_title("Attendance by Student")
    ax.set_xlabel("Student ID")
    ax.set_ylabel("Attendance (%)")
    ax.set_ylim(0, 100)
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    return _save_chart(fig, output_dir, "attendance.png")


def create_marks_distribution_chart(df, output_dir=None):
    """Display the distribution of final marks."""
    output_dir = create_output_directory(output_dir)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["Final_Marks"], bins=8, edgecolor="black")

    ax.set_title("Distribution of Final Marks")
    ax.set_xlabel("Final Marks")
    ax.set_ylabel("Number of Students")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    return _save_chart(fig, output_dir, "marks_distribution.png")


def create_study_vs_marks_chart(df, output_dir=None):
    """Explore the relationship between study hours and final marks."""
    output_dir = create_output_directory(output_dir)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["Study_Hours"], df["Final_Marks"])

    ax.set_title("Study Hours vs Final Marks")
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Final Marks")
    ax.grid(True, linestyle="--", alpha=0.4)

    return _save_chart(fig, output_dir, "study_vs_marks.png")


def create_all_charts(df, output_dir=None):
    """Generate all student performance charts."""
    output_dir = create_output_directory(output_dir)

    chart_functions = [
        create_marks_comparison_chart,
        create_study_hours_chart,
        create_attendance_chart,
        create_marks_distribution_chart,
        create_study_vs_marks_chart,
    ]

    chart_paths = {}

    for chart_function in chart_functions:
        chart_path = chart_function(df, output_dir)
        chart_paths[chart_path.stem] = chart_path

    return chart_paths
