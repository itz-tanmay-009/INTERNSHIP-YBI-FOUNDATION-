"""Project settings and dataset validation functions."""

# Project information
PROJECT_NAME = "Student Performance Analysis"

# Performance thresholds
EXCELLENT_MARKS = 85
GOOD_MARKS = 70
MINIMUM_PASSING_MARKS = 40

# Valid data ranges
MIN_MARKS = 0
MAX_MARKS = 100

MIN_ATTENDANCE = 0
MAX_ATTENDANCE = 100

MIN_STUDY_HOURS = 0

# Supported performance categories
SUPPORTED_CATEGORIES = [
    "Excellent",
    "Good",
    "Needs Improvement"
]


def validate_dataset(df):
    """Validate the structure and values of the student dataset."""

    required_columns = {
        "Student_ID",
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    if df.empty:
        raise ValueError("The dataset is empty.")

    if df["Student_ID"].duplicated().any():
        raise ValueError("Duplicate student IDs found.")

    marks_columns = [
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    ]

    for column in marks_columns:
        if not df[column].between(MIN_MARKS, MAX_MARKS).all():
            raise ValueError(
                f"{column} must contain values between "
                f"{MIN_MARKS} and {MAX_MARKS}."
            )

    if not df["Attendance"].between(
        MIN_ATTENDANCE, MAX_ATTENDANCE
    ).all():
        raise ValueError(
            "Attendance must be between 0 and 100."
        )

    if (df["Study_Hours"] < MIN_STUDY_HOURS).any():
        raise ValueError("Study hours cannot be negative.")

    return True


def generate_data_quality_summary(df):
    """Return a summary of dataset quality checks."""

    if df.empty:
        raise ValueError(
            "Cannot summarize an empty dataset."
        )

    if "Student_ID" not in df.columns:
        raise ValueError(
            "The dataset must contain Student_ID."
        )

    missing_values = int(df.isnull().sum().sum())
    duplicate_ids = int(df["Student_ID"].duplicated().sum())

    summary = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": missing_values,
        "duplicate_student_ids": duplicate_ids,
    }

    summary["data_quality_status"] = (
        "Passed"
        if missing_values == 0 and duplicate_ids == 0
        else "Needs Review"
    )

    return summary