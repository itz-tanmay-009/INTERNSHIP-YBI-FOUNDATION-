
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = [
    "Student_ID",
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]

MARK_COLUMNS = [
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]


def normalize_data(df):
    """Trim column-name whitespace and convert required fields to numbers."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    normalized_columns = [
        column.strip() if isinstance(column, str) else column
        for column in df.columns
    ]
    if pd.Index(normalized_columns).has_duplicates:
        raise ValueError(
            "Column names must be unique after trimming whitespace."
        )

    normalized = df.copy()
    normalized.columns = normalized_columns

    for column in REQUIRED_COLUMNS:
        if column in normalized.columns:
            normalized[column] = pd.to_numeric(
                normalized[column],
                errors="coerce",
            )

    return normalized


def validate_data(df):
    """Validate student records and reject invalid data."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("The dataset is empty.")

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    data = df[REQUIRED_COLUMNS].copy()

    for column in REQUIRED_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")

        if data[column].isna().any():
            raise ValueError(
                f"Column '{column}' contains missing or non-numeric values."
            )

        if not np.isfinite(data[column].to_numpy(dtype=float)).all():
            raise ValueError(
                f"Column '{column}' contains non-finite values."
            )

    if (data["Student_ID"] <= 0).any():
        raise ValueError("Student IDs must be positive.")

    if data["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    if not data["Student_ID"].mod(1).eq(0).all():
        raise ValueError("Student IDs must be whole numbers.")

    if (data["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    for column in MARK_COLUMNS:
        if not data[column].between(0, 100).all():
            raise ValueError(
                f"Values in '{column}' must be between 0 and 100."
            )

    return True


def get_missing_value_summary(df):
    """Count missing values in each column."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    return df.isnull().sum().to_dict()


def get_duplicate_summary(df):
    """Count duplicate rows and duplicate student IDs."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    return {
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_student_ids": (
            int(df["Student_ID"].duplicated().sum())
            if "Student_ID" in df.columns
            else 0
        ),
    }


def get_data_quality_summary(df):
    """Return a summary of common data quality issues."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    missing_columns = sorted(
        set(REQUIRED_COLUMNS) - set(df.columns)
    )

    return {
        "total_records": int(len(df)),
        "total_columns": int(len(df.columns)),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_columns": missing_columns,
        "duplicate_student_ids": (
            int(df["Student_ID"].duplicated().sum())
            if "Student_ID" in df.columns
            else 0
        ),
    }
