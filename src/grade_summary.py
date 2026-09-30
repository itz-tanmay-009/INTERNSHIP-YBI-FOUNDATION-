"""Create a grade-wise summary of student performance."""

import pandas as pd


def assign_grade(marks):
    """Return a grade based on final marks."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"


def create_grade_summary(df):
    """Add grades and return the number of students in each grade."""

    if "Final_Marks" not in df.columns:
        raise ValueError("The dataset must contain Final_Marks.")

    result = df.copy()
    result["Grade"] = result["Final_Marks"].apply(assign_grade)

    summary = (
        result["Grade"]
        .value_counts()
        .reindex(["A", "B", "C", "D", "F"], fill_value=0)
    )

    return result, summary


def save_grade_summary(summary, output_file="grade_summary.csv"):
    """Save the grade summary as a CSV file."""
    summary_df = summary.rename_axis("Grade").reset_index(name="Student_Count")
    summary_df.to_csv(output_file, index=False)
    return output_file