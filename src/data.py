
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_FILE = PROJECT_ROOT / "data" / "student_performance.csv"

COLUMNS = [
    "Student_ID",
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]


def create_sample_data():
    """Create a sample dataset containing 20 student records."""
    records = [
        [1, 2.0, 65, 55, 60, 58],
        [2, 3.0, 72, 62, 68, 65],
        [3, 4.5, 85, 70, 78, 80],
        [4, 1.5, 60, 45, 50, 48],
        [5, 5.0, 92, 82, 88, 90],
        [6, 3.5, 78, 65, 72, 70],
        [7, 1.0, 55, 42, 45, 47],
        [8, 6.0, 96, 88, 92, 95],
        [9, 4.0, 80, 72, 75, 76],
        [10, 2.5, 68, 58, 62, 60],
        [11, 5.5, 90, 80, 85, 87],
        [12, 3.0, 75, 63, 70, 68],
        [13, 4.0, 82, 74, 79, 78],
        [14, 2.0, 62, 50, 55, 52],
        [15, 7.0, 99, 90, 95, 97],
        [16, 3.5, 77, 68, 73, 72],
        [17, 4.5, 88, 76, 82, 84],
        [18, 2.5, 70, 57, 64, 63],
        [19, 5.0, 91, 83, 89, 91],
        [20, 3.0, 78, 66, 71, 69],
    ]

    return pd.DataFrame(records, columns=COLUMNS)


def load_data(file_path=None):
    """Load student records from CSV or use sample data by default."""
    if file_path is not None:
        path = Path(file_path)

        if not path.is_file():
            raise FileNotFoundError(f"Dataset not found: {path}")

        return pd.read_csv(path)

    if DEFAULT_DATA_FILE.is_file():
        return pd.read_csv(DEFAULT_DATA_FILE)

    print("Dataset not found. Using the built-in sample dataset.")
    return create_sample_data()


def get_dataset_overview(df):
    """Return basic information about the dataset."""
    return {
        "total_students": len(df),
        "total_columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def save_data(df, file_path):
    """Save student records to a CSV file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
