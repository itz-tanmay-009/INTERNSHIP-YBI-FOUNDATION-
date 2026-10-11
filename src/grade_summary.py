from pathlib import Path
import pandas as pd

from analysis import get_performance_categories


def create_grade_summary(df):
    categorized = get_performance_categories(df)

    summary = categorized[
        [
            "Student_ID",
            "Previous_Marks",
            "Final_Marks",
            "Performance_Category",
        ]
    ].copy()

    summary["Mark_Change"] = (
        summary["Final_Marks"] - summary["Previous_Marks"]
    ).round(2)

    grade_counts = (
        summary["Performance_Category"]
        .value_counts(sort=False)
        .rename_axis("Performance_Category")
        .reset_index(name="Student_Count")
    )

    grade_average_marks = (
        summary.groupby(
            "Performance_Category", observed=False
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
    if isinstance(average_marks, (str, Path)):
        output_file = average_marks

    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(path, index=False)
    return path