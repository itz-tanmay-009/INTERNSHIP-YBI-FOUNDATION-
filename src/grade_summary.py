
from pathlib import Path

import pandas as pd

from analysis import get_performance_categories


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"


def create_grade_summary(df):
    """Summarize student counts and percentages by performance category."""
    categorized = get_performance_categories(df)

    summary = (
        categorized["Performance_Category"]
        .value_counts(sort=False)
        .rename_axis("Performance_Category")
        .reset_index(name="Student_Count")
    )

    total_students = len(categorized)

    if total_students:
        summary["Percentage"] = (
            summary["Student_Count"] / total_students * 100
        ).round(2)
    else:
        summary["Percentage"] = 0.0

    return summary


def create_student_grade_details(df):
    """Return student IDs, final marks, and performance categories."""
    categorized = get_performance_categories(df)

    columns = [
        "Student_ID",
        "Final_Marks",
        "Performance_Category",
    ]

    return categorized[columns].sort_values(
        by="Final_Marks",
        ascending=False,
        kind="stable",
    ).reset_index(drop=True)


def save_all_grade_summaries(df, output_dir=None):
    """Save category summaries and student grade details to CSV."""
    if output_dir is None:
        output_dir = DEFAULT_OUTPUT_DIR

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = create_grade_summary(df)
    details = create_student_grade_details(df)

    summary_path = output_dir / "grade_summary.csv"
    details_path = output_dir / "student_grade_details.csv"

    summary.to_csv(summary_path, index=False, encoding="utf-8-sig")
    details.to_csv(details_path, index=False, encoding="utf-8-sig")

    return {
        "summary": summary,
        "details": details,
        "summary_path": summary_path,
        "details_path": details_path,
    }
