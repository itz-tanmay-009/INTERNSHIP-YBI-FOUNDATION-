"""Create and export a grade-wise summary of student performance."""

import math


GRADE_ORDER = ["A", "B", "C", "D", "F"]


def validate_marks(marks):
    """Check that marks are numeric, finite, and between 0 and 100."""

    try:
        numeric_marks = float(marks)
    except (TypeError, ValueError):
        raise ValueError("Marks must be a valid number.") from None

    if not math.isfinite(numeric_marks):
        raise ValueError("Marks must be a finite number.")

    if not 0 <= numeric_marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    return numeric_marks


def assign_grade(marks):
    """Return a grade based on final marks."""

    marks = validate_marks(marks)

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
    """Add grades and return the student data and grade counts."""

    if df.empty:
        raise ValueError("Cannot create a summary from an empty dataset.")

    if "Final_Marks" not in df.columns:
        raise ValueError("The dataset must contain Final_Marks.")

    result = df.copy()

    # Validate every mark before assigning grades.
    result["Final_Marks"] = result["Final_Marks"].apply(validate_marks)
    result["Grade"] = result["Final_Marks"].apply(assign_grade)

    summary = (
        result["Grade"]
        .value_counts()
        .reindex(GRADE_ORDER, fill_value=0)
    )

    return result, summary


def save_grade_summary(summary, output_file="grade_summary.csv"):
    """Save grade counts and percentages to a CSV file."""

    total_students = summary.sum()

    percentages = (
        summary.div(total_students).mul(100)
        if total_students > 0
        else summary.astype(float)
    )

    summary_df = summary.rename("Student_Count").to_frame()
    summary_df["Percentage"] = percentages.round(2)
    summary_df.index.name = "Grade"

    summary_df.to_csv(output_file)
    return output_file


def save_student_grades(df, output_file="student_grades.csv"):
    """Save each student's ID, final marks, and assigned grade."""

    required_columns = {"Student_ID", "Final_Marks"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    student_data = df[["Student_ID", "Final_Marks"]].copy()
    student_data["Final_Marks"] = student_data["Final_Marks"].apply(
        validate_marks
    )
    student_data["Grade"] = student_data["Final_Marks"].apply(assign_grade)

    student_data.to_csv(output_file, index=False)
    return output_file