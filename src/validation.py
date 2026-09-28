"""Project configuration and dataset validation for student performance analysis."""

# Project information
PROJECT_NAME = "Student Performance Analysis"

# Performance thresholds
EXCELLENT_MARKS = 85
GOOD_MARKS = 70
MINIMUM_PASSING_MARKS = 40

# Data validation limits
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

    # Required columns
    required_columns = {
        "Student_ID",
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    }

    # Check for missing columns
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    # Check whether the dataset is empty
    if df.empty:
        raise ValueError("The student dataset is empty.")

    # Check for duplicate student IDs
    if df["Student_ID"].duplicated().any():
        raise ValueError("Duplicate Student_ID values found.")

    # Validate marks
    marks_columns = [
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    ]

    for column in marks_columns:
        if not df[column].between(MIN_MARKS, MAX_MARKS).all():
            raise ValueError(
                f"{column} must be between {MIN_MARKS} and {MAX_MARKS}."
            )

    # Validate attendance
    if not df["Attendance"].between(
        MIN_ATTENDANCE,
        MAX_ATTENDANCE
    ).all():
        raise ValueError(
            f"Attendance must be between "
            f"{MIN_ATTENDANCE} and {MAX_ATTENDANCE}."
        )

    # Validate study hours
    if (df["Study_Hours"] < MIN_STUDY_HOURS).any():
        raise ValueError("Study hours cannot be negative.")

    return True