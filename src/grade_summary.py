from pathlib import Path
import pandas as pd

from analysis import (
    get_performance_categories,
    compare_previous_and_final_marks,
)


def create_grade_summary(df):
    """Create student-level and category-level summaries."""
    categorized = get_performance_categories(df)

    comparison = compare_previous_and_final_marks(df)

    summary = categorized[
        [
            "Student_ID",
            "Previous_Marks",
            "Assignment_Marks",
            "Final_Marks",
            "Performance_Category",
        ]
    ].copy()

    summary = summary.merge(
        comparison[
            ["Student_ID", "Mark_Change", "Improvement_Status"]
        ],
        on="Student_ID",
        how="left",
        validate="one_to_one",
    )

    grade_counts = (
        summary.groupby(
            "Performance_Category",
            observed=False,
        )
        .size()
        .rename("Student_Count")
        .reset_index()
    )

    grade_average_marks = (
        summary.groupby(
            "Performance_Category",
            observed=False,
        )["Final_Marks"]
        .mean()
        .round(2)
        .rename("Average_Final_Marks")
        .reset_index()
    )

    return summary, grade_counts, grade_average_marks


def save_grade_summary(
    summary,
    average_marks=None,
    output_file="grade_summary.csv",
):
    """Save a summary DataFrame as a CSV file."""
    if isinstance(average_marks, (str, Path)):
        output_file = average_marks

    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(path, index=False)

    return path


def save_all_grade_summaries(df, output_dir="output"):
    """Save all grade-summary CSV files."""
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    summary, counts, averages = create_grade_summary(df)

    save_grade_summary(
        summary,
        output_file=directory / "grade_summary.csv",
    )

    counts.to_csv(directory / "grade_counts.csv", index=False)
    averages.to_csv(
        directory / "grade_average_marks.csv",
        index=False,
    )

    return {
        "summary": directory / "grade_summary.csv",
        "counts": directory / "grade_counts.csv",
        "averages": directory / "grade_average_marks.csv",
    }