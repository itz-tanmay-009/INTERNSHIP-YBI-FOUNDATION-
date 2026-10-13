from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from analysis import get_performance_categories


def save_chart(fig, output_file=None):
    """Save a chart and close the figure."""
    if output_file:
        path = Path(output_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=150, bbox_inches="tight")

    plt.close(fig)


def plot_marks_distribution(df, output_file=None):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(
        df["Final_Marks"],
        bins=8,
        edgecolor="black",
    )
    ax.set_title("Distribution of Final Marks")
    ax.set_xlabel("Final Marks")
    ax.set_ylabel("Number of Students")
    ax.grid(axis="y", alpha=0.25)

    save_chart(fig, output_file)


def plot_study_hours_vs_marks(df, output_file=None):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(df["Study_Hours"], df["Final_Marks"])
    ax.set_title("Study Hours and Final Marks")
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Final Marks")
    ax.grid(alpha=0.25)

    save_chart(fig, output_file)


def plot_attendance_vs_marks(df, output_file=None):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(df["Attendance"], df["Final_Marks"])
    ax.set_title("Attendance and Final Marks")
    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Final Marks")
    ax.grid(alpha=0.25)

    save_chart(fig, output_file)


def plot_previous_vs_final_marks(df, output_file=None):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(df["Previous_Marks"], df["Final_Marks"])

    lower = min(
        df["Previous_Marks"].min(),
        df["Final_Marks"].min(),
    )
    upper = max(
        df["Previous_Marks"].max(),
        df["Final_Marks"].max(),
    )

    ax.plot(
        [lower, upper],
        [lower, upper],
        linestyle="--",
    )

    ax.set_title("Previous Marks and Final Marks")
    ax.set_xlabel("Previous Marks")
    ax.set_ylabel("Final Marks")
    ax.grid(alpha=0.25)

    save_chart(fig, output_file)


def plot_performance_categories(df, output_file=None):
    categorized = get_performance_categories(df)

    counts = categorized["Performance_Category"].value_counts(
        sort=False
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    counts.plot(kind="bar", ax=ax, edgecolor="black")

    ax.set_title("Student Performance Categories")
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Students")
    ax.tick_params(axis="x", rotation=20)

    save_chart(fig, output_file)


def plot_mark_change(df, output_file=None):
    fig, ax = plt.subplots(figsize=(10, 5))

    change = df["Final_Marks"] - df["Previous_Marks"]

    ax.bar(df["Student_ID"].astype(str), change)
    ax.axhline(0, linestyle="--")
    ax.set_title("Change in Marks for Each Student")
    ax.set_xlabel("Student ID")
    ax.set_ylabel("Final Marks - Previous Marks")

    save_chart(fig, output_file)


def create_all_charts(df, output_dir="output/charts"):
    """Generate and save all six project charts."""
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    chart_functions = {
        "marks_distribution": plot_marks_distribution,
        "study_hours_vs_marks": plot_study_hours_vs_marks,
        "attendance_vs_marks": plot_attendance_vs_marks,
        "previous_vs_final_marks": plot_previous_vs_final_marks,
        "performance_categories": plot_performance_categories,
        "mark_change": plot_mark_change,
    }

    saved_paths = {}

    for name, function in chart_functions.items():
        path = directory / f"{name}.png"
        function(df, path)
        saved_paths[name] = path

    return saved_paths