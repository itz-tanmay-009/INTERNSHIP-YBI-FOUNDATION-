
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_FILE = PROJECT_ROOT / "data" / "student_performance.csv"


def create_sample_data():
    """Create a sample dataset containing 20 student records."""
    data = {
        "Student_ID": list(range(1, 21)),
        "Study_Hours": [
            2, 3, 1, 5, 4, 2, 1, 6, 3, 5,
            4, 2, 7, 3, 8, 4, 6, 2, 5, 3,
        ],
        "Attendance": [
            70, 80, 60, 90, 85, 75, 55, 95, 78, 88,
            82, 72, 98, 76, 96, 84, 91, 68, 89, 79,
        ],
        "Previous_Marks": [
            50, 60, 45, 70, 65, 55, 35, 75, 58, 72,
            68, 48, 80, 57, 85, 63, 77, 42, 74, 59,
        ],
        "Assignment_Marks": [
            55, 65, 50, 75, 70, 60, 40, 80, 62, 78,
            72, 53, 85, 61, 90, 68, 82, 47, 79, 64,
        ],
        "Final_Marks": [
            60, 70, 55, 80, 75, 65, 47, 85, 68, 82,
            76, 58, 92, 64, 97, 72, 88, 52, 84, 69,
        ],
    }

    return pd.DataFrame(data)


def load_data(file_path=None):
    """Load student records from a CSV file or use sample data."""
    if file_path is None:
        file_path = DEFAULT_DATA_FILE

        if not file_path.is_file():
            return create_sample_data()

    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    if file_path.suffix.lower() != ".csv":
        raise ValueError("The dataset must be a CSV file.")

    return pd.read_csv(file_path, encoding="utf-8-sig")


def get_dataset_overview(df):
    """Return a concise overview of the dataset."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    return {
        "total_records": int(len(df)),
        "total_columns": int(len(df.columns)),
        "column_names": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage_bytes": int(
            df.memory_usage(index=True, deep=True).sum()
        ),
    }


def save_data(df, file_path=None):
    """Save student records to a CSV file."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if file_path is None:
        file_path = DEFAULT_DATA_FILE

    file_path = Path(file_path)
    if file_path.suffix.lower() != ".csv":
        raise ValueError("The dataset must be saved as a CSV file.")

    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False, encoding="utf-8-sig")

    return file_path


def get_column_summary(df):
    """Summarize each column's data type and missing values."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    return pd.DataFrame({
        "Column": df.columns,
        "Data_Type": [
            str(df[column].dtype) for column in df.columns
        ],
        "Missing_Values": [
            int(df[column].isnull().sum()) for column in df.columns
        ],
        "Unique_Values": [
            int(df[column].nunique(dropna=True))
            for column in df.columns
        ],
    })
