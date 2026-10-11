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
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("The dataset is empty.")

    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    data = df[REQUIRED_COLUMNS].copy()

    if data.isnull().any().any():
        raise ValueError("The dataset contains missing values.")

    for column in REQUIRED_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="raise")

    if not np.isfinite(data.to_numpy(dtype=float)).all():
        raise ValueError("The dataset contains invalid numeric values.")

    if data["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    if (data["Student_ID"] <= 0).any():
        raise ValueError("Student IDs must be positive.")

    if (data["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    for column in MARK_COLUMNS:
        if not data[column].between(0, 100).all():
            raise ValueError(f"{column} must be between 0 and 100.")

    return True


def get_data_quality_summary(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_student_ids": (
            int(df["Student_ID"].duplicated().sum())
            if "Student_ID" in df.columns
            else None
        ),
    }