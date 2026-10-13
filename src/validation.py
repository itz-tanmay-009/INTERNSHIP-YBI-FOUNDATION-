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


def validate_data(df):
    """Check the student dataset before analysis."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("The dataset contains no records.")

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    data = df[REQUIRED_COLUMNS].copy()

    if data.isnull().any().any():
        raise ValueError("Please fix missing values before analysis.")

    for column in REQUIRED_COLUMNS:
        try:
            data[column] = pd.to_numeric(
                data[column], errors="raise"
            )
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"Column '{column}' must contain numbers."
            ) from exc

    if not np.isfinite(data.to_numpy(dtype=float)).all():
        raise ValueError("The dataset contains invalid numeric values.")

    if data["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must not be duplicated.")

    if (data["Student_ID"] <= 0).any():
        raise ValueError("Student IDs must be positive.")

    if (data["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    for column in MARK_COLUMNS:
        if not data[column].between(0, 100).all():
            raise ValueError(
                f"Values in '{column}' must be between 0 and 100."
            )

    return True


def get_data_quality_summary(df):
    """Summarize common data-quality issues."""
    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_student_ids": (
            int(df["Student_ID"].duplicated().sum())
            if "Student_ID" in df.columns
            else None
        ),
    }


def remove_duplicate_rows(df):
    """Return a copy with fully duplicated rows removed."""
    return df.drop_duplicates().reset_index(drop=True)