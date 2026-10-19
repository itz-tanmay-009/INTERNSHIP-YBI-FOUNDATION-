
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
    """Validate student data before performing analysis."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("The dataset contains no records.")

    missing = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    data = df[REQUIRED_COLUMNS].copy()

    if data.isnull().any().any():
        raise ValueError("The dataset contains missing values.")

    for column in REQUIRED_COLUMNS:
        try:
            data[column] = pd.to_numeric(
                data[column], errors="raise"
            )
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"Column '{column}' must contain numeric values."
            ) from exc

    if not np.isfinite(data.to_numpy(dtype=float)).all():
        raise ValueError("The dataset contains invalid numeric values.")

    if (data["Student_ID"] <= 0).any():
        raise ValueError("Student IDs must be positive.")

    if data["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

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
            if "Student_ID" in df.columns else None
        ),
    }


def remove_duplicate_rows(df):
    """Remove fully duplicated records from a copy."""
    return df.drop_duplicates().reset_index(drop=True)


def get_missing_value_summary(df):
    """Count missing values in each column."""
    missing = df.isnull().sum()
    return missing[missing > 0].to_dict()


def check_mark_ranges(df):
    """Check that marks and attendance are between 0 and 100."""
    results = {}

    for column in MARK_COLUMNS:
        if column not in df.columns:
            results[column] = "Column missing"
            continue

        values = pd.to_numeric(df[column], errors="coerce")
        valid = values.notna() & values.between(0, 100)

        results[column] = (
            "Valid" if valid.all() else "Invalid values found"
        )

    return results


def get_validation_report(df):
    """Return a compact validation report."""
    return {
        "dataset_is_empty": df.empty,
        "missing_columns": [
            column for column in REQUIRED_COLUMNS
            if column not in df.columns
        ],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "mark_range_checks": check_mark_ranges(df),
    }
