
from pathlib import Path

from analysis import (
    calculate_averages,
    calculate_pass_percentage,
    get_top_student,
    get_lowest_student,
    get_grade_counts,
    get_improvement_summary,
    get_correlation_matrix,
    generate_insights,
)


def generate_report(df):
    """Generate a readable student performance report."""
    if df.empty:
        raise ValueError("Cannot generate a report from an empty dataset.")

    averages = calculate_averages(df)
    top = get_top_student(df)
    lowest = get_lowest_student(df)
    grade_counts = get_grade_counts(df)
    improvement = get_improvement_summary(df)
    correlations = get_correlation_matrix(df)

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
        "4. PERFORMANCE CATEGORIES",
        "-" * 60,
    ]

    for category, count in grade_counts.items():
        lines.append(f"{category}: {count} students")

    lines.extend([
        "",
        "5. CORRELATION WITH FINAL MARKS",
        "-" * 60,
    ])

    for column in correlations.columns:
        if column != "Final_Marks":
            value = correlations.loc[column, "Final_Marks"]
            lines.append(f"{column}: {value:.2f}")

    lines.extend([
        "",
        "6. AUTOMATED INSIGHTS",
        "-" * 60,
    ])

    lines.extend(f"- {item}" for item in generate_insights(df))

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
    report_text,
    output_file="output/student_performance_report.txt",
):
    """Save the report as a UTF-8 text file."""
    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report_text, encoding="utf-8")
    return path


def generate_and_save_report(
    df,
    output_file="output/student_performance_report.txt",
):
    """Generate and save the report in one step."""
    report_text = generate_report(df)
    return save_report(report_text, output_file)
