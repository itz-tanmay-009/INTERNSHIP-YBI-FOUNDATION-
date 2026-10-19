
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
    """Validate the structure and values of the student dataset."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("The dataset is empty.")

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError("The dataset contains missing values.")

    for column in REQUIRED_COLUMNS:
        try:
            values = pd.to_numeric(df[column], errors="raise")
        except (ValueError, TypeError) as error:
            raise ValueError(
                f"Column '{column}' must contain numeric values."
            ) from error

        if not np.isfinite(values.to_numpy(dtype=float)).all():
            raise ValueError(
                f"Column '{column}' contains non-finite values."
            )

    if (df["Student_ID"] <= 0).any():
        raise ValueError("Student IDs must be positive.")

    if df["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    if (df["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    for column in MARK_COLUMNS:
        if not df[column].between(0, 100).all():
            raise ValueError(
                f"Values in '{column}' must be between 0 and 100."
            )

    return True


def get_data_quality_summary(df):
    """Return a summary of dataset quality."""
    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_student_ids": (
            int(df["Student_ID"].duplicated().sum())
            if "Student_ID" in df.columns else 0
        ),
        "column_names": list(df.columns),
    }


def remove_duplicate_rows(df):
    """Return a copy of the dataset without duplicate rows."""
    return df.drop_duplicates().reset_index(drop=True)


def get_missing_value_summary(df):
    """Count missing values in each column."""
    return df.isnull().sum().to_dict()


def check_mark_ranges(df):
    """Check whether marks and attendance are within valid ranges."""
    results = {}

    for column in MARK_COLUMNS:
        if column not in df.columns:
            results[column] = False
            continue

        values = pd.to_numeric(df[column], errors="coerce")
        results[column] = bool(
            values.notna().all()
            and np.isfinite(values.to_numpy(dtype=float)).all()
            and values.between(0, 100).all()
        )

    return results


def get_validation_report(df):
    """Generate a report describing data validation results."""
    report = {
        "is_dataframe": isinstance(df, pd.DataFrame),
        "is_empty": True,
        "missing_columns": [],
        "missing_values": 0,
        "duplicate_rows": 0,
        "mark_ranges_valid": {},
        "valid": False,
        "errors": [],
    }

    if not isinstance(df, pd.DataFrame):
        report["errors"].append(
            "Input must be a pandas DataFrame."
        )
        return report

    report["is_empty"] = df.empty
    report["missing_columns"] = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]
    report["missing_values"] = int(df.isnull().sum().sum())
    report["duplicate_rows"] = int(df.duplicated().sum())
    report["mark_ranges_valid"] = check_mark_ranges(df)

    try:
        validate_data(df)
        report["valid"] = True
    except (ValueError, TypeError) as error:
        report["errors"].append(str(error))

    return report
