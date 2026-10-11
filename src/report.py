from pathlib import Path

from analysis import (
    calculate_averages,
    calculate_average_improvement,
    calculate_pass_percentage,
    find_top_three_students,
    generate_insights,
    get_correlation_matrix,
    get_grade_counts,
    get_lowest_student,
    get_top_student,
)


def generate_report(df):
    averages = calculate_averages(df)
    top = get_top_student(df)
    lowest = get_lowest_student(df)
    top_three = find_top_three_students(df)
    grade_counts = get_grade_counts(df)
    correlations = get_correlation_matrix(df)

    lines = [
        "=" * 60,
        "STUDENT PERFORMANCE ANALYSIS REPORT",
        "=" * 60,
        "",
        "DATASET OVERVIEW",
        "-" * 60,
        f"Total students: {len(df)}",
        f"Average study hours: {averages['Study_Hours']:.2f}",
        f"Average attendance: {averages['Attendance']:.2f}%",
        f"Average previous marks: {averages['Previous_Marks']:.2f}",
        f"Average assignment marks: {averages['Assignment_Marks']:.2f}",
        f"Average final marks: {averages['Final_Marks']:.2f}",
        "",
        "PASSING AND IMPROVEMENT",
        "-" * 60,
        f"Pass percentage: {calculate_pass_percentage(df):.2f}%",
        (
            "Average mark change: "
            f"{calculate_average_improvement(df):.2f}"
        ),
        "",
        "HIGHEST SCORER",
        "-" * 60,
        f"Student {int(top['Student_ID'])}: {top['Final_Marks']:.0f} marks",
        "",
        "LOWEST SCORER",
        "-" * 60,
        (
            f"Student {int(lowest['Student_ID'])}: "
            f"{lowest['Final_Marks']:.0f} marks"
        ),
        "",
        "TOP THREE STUDENTS",
        "-" * 60,
    ]

    for rank, (_, student) in enumerate(top_three.iterrows(), start=1):
        lines.append(
            f"{rank}. Student {int(student['Student_ID'])}: "
            f"{student['Final_Marks']:.0f} marks"
        )

    lines.extend(["", "PERFORMANCE CATEGORY COUNTS", "-" * 60])

    for category, count in grade_counts.items():
        lines.append(f"{category}: {count}")

    lines.extend(["", "CORRELATION WITH FINAL MARKS", "-" * 60])

    for column in correlations.columns:
        if column != "Final_Marks":
            lines.append(
                f"{column}: {correlations.loc[column, 'Final_Marks']:.2f}"
            )

    lines.extend(["", "AUTOMATED INSIGHTS", "-" * 60])
    lines.extend(f"- {item}" for item in generate_insights(df))

    lines.extend([
        "",
        "INTERPRETATION NOTE",
        "-" * 60,
        "Correlation indicates association, not causation.",
        "Results depend on dataset quality and sample size.",
        "Synthetic data should not be treated as real-world evidence.",
        "",
        "=" * 60,
    ])

    return "\n".join(lines)


def save_report(
    report_text,
    output_file="output/student_performance_report.txt",
):
    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report_text, encoding="utf-8")
    return path