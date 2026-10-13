from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "student_performance.csv"


def load_data(file_path=None):
    """Load student records from a CSV file."""
    path = Path(file_path) if file_path else DATA_FILE

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}. "
            "Please provide your student performance CSV file."
        )

    return pd.read_csv(path)


def get_dataset_overview(df):
    """Return basic information about the dataset."""
    return {
        "total_students": len(df),
        "total_columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def filter_students(df, minimum_marks=None, minimum_attendance=None):
    """Filter students using marks and attendance criteria."""
    result = df.copy()

    if minimum_marks is not None:
        result = result[
            result["Final_Marks"] >= minimum_marks
        ]

    if minimum_attendance is not None:
        result = result[
            result["Attendance"] >= minimum_attendance
        ]

    return result.reset_index(drop=True)


def save_data(df, file_path):
    """Save data to a CSV file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path