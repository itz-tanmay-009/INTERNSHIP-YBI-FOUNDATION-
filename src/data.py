from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "student_performance.csv"

COLUMNS = [
    "Student_ID",
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]


def create_sample_data():
    records = [
        [1, 2, 65, 55, 60, 58],
        [2, 3, 70, 60, 65, 63],
        [3, 4, 75, 65, 70, 68],
        [4, 5, 80, 70, 75, 74],
        [5, 6, 85, 75, 80, 79],
        [6, 3, 72, 62, 67, 65],
        [7, 1, 50, 45, 50, 47],
        [8, 7, 90, 82, 88, 90],
        [9, 4, 78, 68, 73, 71],
        [10, 5, 82, 72, 77, 76],
        [11, 6, 88, 80, 84, 86],
        [12, 2, 60, 52, 57, 55],
        [13, 8, 95, 88, 92, 95],
        [14, 4, 76, 67, 72, 70],
        [15, 9, 98, 92, 96, 97],
        [16, 3, 68, 58, 63, 61],
        [17, 5, 84, 74, 79, 78],
        [18, 7, 92, 85, 90, 92],
        [19, 2, 63, 54, 59, 56],
        [20, 6, 86, 78, 82, 84],
    ]
    return pd.DataFrame(records, columns=COLUMNS)


def load_data(file_path=None):
    path = Path(file_path) if file_path else DATA_FILE
    if path.exists():
        return pd.read_csv(path)
    return create_sample_data()


def save_data(df, file_path=None):
    path = Path(file_path) if file_path else DATA_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path