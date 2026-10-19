
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_FILE = PROJECT_ROOT / "data" / "student_performance.csv"


def create_sample_data():
    """Create sample records for testing when no CSV is available."""
    return pd.DataFrame({
        "Student_ID": list(range(1, 21)),
        "Study_Hours": [
            2.0, 3.5, 5.0, 4.0, 6.5,
            1.5, 2.5, 7.0, 3.0, 5.5,
            4.5, 6.0, 2.0, 8.0, 7.5,
            3.5, 5.0, 1.0, 6.5, 4.0,
        ],
        "Attendance": [
            65, 72, 85, 78, 92,
            55, 68, 95, 70, 88,
            82, 90, 60, 98, 96,
            75, 84, 50, 93, 80,
        ],
        "Previous_Marks": [
            45, 55, 68, 60, 75,
            35, 48, 80, 52, 72,
            65, 78, 40, 85, 90,
            58, 70, 30, 82, 62,
        ],
        "Assignment_Marks": [
            50, 60, 72, 65, 80,
            40, 52, 85, 58, 76,
            70, 82, 45, 90, 94,
            62, 75, 35, 88, 68,
        ],
        "Final_Marks": [
            48, 58, 74, 66, 84,
            38, 47, 88, 55, 79,
            72, 85, 43, 93, 97,
            64, 77, 32, 91, 70,
        ],
    })


def load_data(file_path=None):
    """Load student data from CSV or use sample records."""
    path = Path(file_path) if file_path else DEFAULT_DATA_FILE

    if path.exists():
        return pd.read_csv(path)

    if file_path is not None:
        raise FileNotFoundError(f"Dataset not found: {path}")

    print("CSV not found. Using sample data for testing.")
    return create_sample_data()


def get_dataset_overview(df):
    """Return basic information about the dataset."""
    return {
        "total_students": len(df),
        "total_columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def save_data(df, file_path):
    """Save student records to a CSV file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
