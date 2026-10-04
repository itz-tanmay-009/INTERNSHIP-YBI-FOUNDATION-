"""Generate a text report for student performance analysis."""

from validation import MINIMUM_PASSING_MARKS


GRADE_ORDER = ["A", "B", "C", "D", "F"]


def generate_report(df, output_file="student_performance_report.txt"):
    """Create and save a summary report from the student dataset."""

    if df.empty:
        raise ValueError("Cannot generate a report from an empty dataset.")

    required_columns = {
        "Student_ID",
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Final_Marks",
    }

    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    highest = df.loc[df["Final_Marks"].idxmax()]
    lowest = df.loc[df["Final_Marks"].idxmin()]

    passed = df["Final_Marks"].ge(MINIMUM_PASSING_MARKS).sum()
    failed = len(df) - passed
    pass_percentage = (passed / len(df)) * 100

    lines = [
        "STUDENT PERFORMANCE REPORT",
        "=" * 40,
        f"Total students: {len(df)}",
        f"Average study hours: {df['Study_Hours'].mean():.2f}",
        f"Average attendance: {df['Attendance'].mean():.2f}%",
        f"Average assignment score: {df['Assignment_Score'].mean():.2f}",
        f"Average final marks: {df['Final_Marks'].mean():.2f}",
        "",
        "PASS / FAIL SUMMARY",
        "-" * 40,
        f"Passed students: {passed}",
        f"Failed students: {failed}",
        f"Pass percentage: {pass_percentage:.2f}%",
        "",
        "TOP PERFORMANCE",
        "-" * 40,
        f"Student ID: {int(highest['Student_ID'])}",
        f"Final marks: {highest['Final_Marks']}",
        "",
        "LOWEST PERFORMANCE",
        "-" * 40,
        f"Student ID: {int(lowest['Student_ID'])}",
        f"Final marks: {lowest['Final_Marks']}",
    ]

    if "Performance_Category" in df.columns:
        lines.extend(["", "PERFORMANCE CATEGORIES", "-" * 40])

        category_counts = df["Performance_Category"].value_counts()
        for category, count in category_counts.items():
            lines.append(f"{category}: {count} student(s)")

    if "Grade" in df.columns:
        lines.extend(["", "GRADE-WISE SUMMARY", "-" * 40])

        grade_counts = (
            df["Grade"]
            .value_counts()
            .reindex(GRADE_ORDER, fill_value=0)
        )

        for grade, count in grade_counts.items():
            percentage = count / len(df) * 100
            lines.append(
                f"Grade {grade}: {count} student(s) ({percentage:.2f}%)"
            )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return output_file