
import math
from pathlib import Path

import pandas as pd

from analysis import (
    calculate_averages,
    calculate_pass_percentage,
    get_top_student,
    get_lowest_student,
    get_grade_counts,
    get_improvement_summary,
    get_correlation_matrix,
    get_score_distribution,
    get_attendance_summary,
    get_study_hours_summary,
    generate_insights,
)


DEFAULT_REPORT_FILE = (
    Path(__file__).resolve().parent.parent
    / "output"
    / "student_performance_report.txt"
)


def generate_report(df: pd.DataFrame) -> str:
    """Generate a detailed student performance report."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("Cannot generate a report from an empty dataset.")

    averages = calculate_averages(df)
    top = get_top_student(df)
    lowest = get_lowest_student(df)
    categories = get_grade_counts(df)
    improvement = get_improvement_summary(df)
    score_distribution = get_score_distribution(df)
    correlations = get_correlation_matrix(df)
    attendance = get_attendance_summary(df)
    study = get_study_hours_summary(df)

    lines = [
        "=" * 60,
        "STUDENT PERFORMANCE ANALYSIS REPORT",
        "=" * 60,
        "",
        "1. DATASET SUMMARY",
        "-" * 60,
        f"Total students: {len(df)}",
        f"Average study hours: {averages['Study_Hours']:.2f}",
        f"Average attendance: {averages['Attendance']:.2f}%",
        f"Average previous marks: {averages['Previous_Marks']:.2f}",
        f"Average assignment marks: {averages['Assignment_Marks']:.2f}",
        f"Average final marks: {averages['Final_Marks']:.2f}",
        "",
        "2. EXAM RESULTS",
        "-" * 60,
        f"Pass percentage: {calculate_pass_percentage(df):.2f}%",
        (
            f"Highest scorer: Student {int(top['Student_ID'])}, "
            f"{top['Final_Marks']:.0f} marks"
        ),
        (
            f"Lowest scorer: Student {int(lowest['Student_ID'])}, "
            f"{lowest['Final_Marks']:.0f} marks"
        ),
        "",
        "3. MARK IMPROVEMENT",
        "-" * 60,
        f"Improved students: {improvement['improved_students']}",
        f"Declined students: {improvement['declined_students']}",
        f"Unchanged students: {improvement['unchanged_students']}",
        f"Average mark change: {improvement['average_mark_change']:.2f}",
        "",
        "4. ATTENDANCE AND STUDY HABITS",
        "-" * 60,
        f"Average attendance: {attendance['average_attendance']:.2f}%",
        f"Median attendance: {attendance['median_attendance']:.2f}%",
        (
            "Students below 75% attendance: "
            f"{attendance['low_attendance_students']}"
        ),
        f"Average study hours: {study['average_study_hours']:.2f}",
        f"Median study hours: {study['median_study_hours']:.2f}",
        (
            "Students studying under 2 hours: "
            f"{study['low_study_hours_students']}"
        ),
        "",
        "5. PERFORMANCE CATEGORIES",
        "-" * 60,
    ]

    for category, count in categories.items():
        lines.append(f"{category}: {count} students")

    lines.extend([
        "",
        "6. FINAL MARKS DISTRIBUTION",
        "-" * 60,
    ])

    lines.extend(
        f"{range_name}: {count} students"
        for range_name, count in score_distribution.items()
    )

    lines.extend([
        "",
        "7. CORRELATION WITH FINAL MARKS",
        "-" * 60,
    ])

    for column in correlations.columns:
        if column != "Final_Marks":
            value = correlations.loc[column, "Final_Marks"]
            formatted_value = (
                f"{value:.2f}" if math.isfinite(float(value)) else "N/A"
            )
            lines.append(f"{column}: {formatted_value}")

    lines.extend([
        "",
        "8. AUTOMATED INSIGHTS",
        "-" * 60,
    ])

    lines.extend(f"- {insight}" for insight in generate_insights(df))

    lines.extend([
        "",
        "NOTES",
        "-" * 60,
        "Correlation does not prove cause and effect.",
        "Results depend on the quality of the dataset.",
        "Sample data may not represent real student performance.",
        "",
        "=" * 60,
        "END OF REPORT",
        "=" * 60,
    ])

    return "\n".join(lines)


def save_report(
    report_text: str,
    output_file: str | Path = DEFAULT_REPORT_FILE,
) -> Path:
    """Save the report as a UTF-8 text file."""
    if not isinstance(report_text, str):
        raise TypeError("Report content must be a string.")

    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report_text.rstrip() + "\n", encoding="utf-8")
    return path


def generate_and_save_report(
    df: pd.DataFrame,
    output_file: str | Path = DEFAULT_REPORT_FILE,
) -> Path:
    """Generate and save a report in one operation."""
    text = generate_report(df)
    return save_report(text, output_file)
