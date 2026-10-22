
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
    """Convert required numeric columns without mutating the input."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    result = df.copy()

    for column in REQUIRED_COLUMNS:
        if column not in result.columns:
            continue

        try:
            result[column] = pd.to_numeric(result[column], errors="raise")
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Column '{column}' contains non-numeric values."
            ) from error

    return result


def validate_data(df):
    """Validate student data and raise errors for invalid records."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("The dataset is empty.")

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError("The dataset contains missing required values.")

    numeric_columns = {}

    for column in REQUIRED_COLUMNS:
        numeric_values = pd.to_numeric(df[column], errors="coerce")

        if numeric_values.isnull().any():
            raise ValueError(
                f"Column '{column}' contains non-numeric values."
            )

        if not np.isfinite(numeric_values.to_numpy(dtype=float)).all():
            raise ValueError(
                f"Column '{column}' contains non-finite values."
            )

        numeric_columns[column] = numeric_values

    student_ids = numeric_columns["Student_ID"]

    if (student_ids <= 0).any():
        raise ValueError("Student IDs must be positive.")

    if (student_ids % 1 != 0).any():
        raise ValueError("Student IDs must be whole numbers.")

    if student_ids.duplicated().any():
        raise ValueError("Student IDs must be unique.")

    if (numeric_columns["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    for column in MARK_COLUMNS:
        if not numeric_columns[column].between(0, 100).all():
            raise ValueError(
                f"Values in '{column}' must be between 0 and 100."
            )

    return True


def get_missing_value_summary(df):
    """Count missing values in each column."""
    return df.isnull().sum().to_dict()


def get_duplicate_summary(df):
    """Count duplicate rows and duplicate student IDs."""
    return {
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_student_ids": int(
            df["Student_ID"].duplicated().sum()
        ) if "Student_ID" in df.columns else 0,
    }


def get_data_quality_summary(df):
    """Return a summary of basic dataset quality checks."""
    return {
        "total_rows": len(df),
        "total_records": len(df),
        "total_columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_columns": sorted(
            set(REQUIRED_COLUMNS) - set(df.columns)
        ),
    }
