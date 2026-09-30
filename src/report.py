"""Generate a text report for student performance analysis."""

from validation import MINIMUM_PASSING_MARKS


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
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    highest = df.loc[df["Final_Marks"].idxmax()]
    lowest = df.loc[df["Final_Marks"].idxmin()]

    passed = df["Final_Marks"].ge(MINIMUM_PASSING_MARKS).sum()
    failed = len(df) - passed
    pass_percentage = (passed / len(df)) * 100

    lines = [
        "STUDENT PERFORMANCE REPORT",
        "=" * 35,
        f"Total students: {len(df)}",
        f"Average study hours: {df['Study_Hours'].mean():.2f}",
        f"Average attendance: {df['Attendance'].mean():.2f}%",
        f"Average assignment score: {df['Assignment_Score'].mean():.2f}",
        f"Average final marks: {df['Final_Marks'].mean():.2f}",
        "",
        "PASS / FAIL SUMMARY",
        f"Passed students: {passed}",
        f"Failed students: {failed}",
        f"Pass percentage: {pass_percentage:.2f}%",
        "",
        "TOP PERFORMANCE",
        f"Student ID: {int(highest['Student_ID'])}",
        f"Final marks: {highest['Final_Marks']}",
        "",
        "LOWEST PERFORMANCE",
        f"Student ID: {int(lowest['Student_ID'])}",
        f"Final marks: {lowest['Final_Marks']}",
    ]

    if "Performance_Category" in df.columns:
        lines.extend(["", "PERFORMANCE CATEGORIES"])
        for category, count in df["Performance_Category"].value_counts().items():
            lines.append(f"{category}: {count} student(s)")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return output_file