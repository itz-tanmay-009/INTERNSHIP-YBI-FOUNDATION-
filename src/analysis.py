
from typing import Final

import pandas as pd


PASS_MARK: Final = 40

NUMERIC_COLUMNS = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]

PERFORMANCE_BINS = [0, 40, 60, 80, 100.001]
PERFORMANCE_LABELS = [
    "Needs Improvement",
    "Satisfactory",
    "Good",
    "Excellent",
]


def calculate_averages(df: pd.DataFrame) -> dict:
    """Calculate averages for numerical columns."""
    return df[NUMERIC_COLUMNS].mean().round(2).to_dict()


def get_top_student(df: pd.DataFrame) -> dict:
    """Return the highest-scoring student."""
    if df.empty:
        raise ValueError("No student records are available.")

    position = df["Final_Marks"].reset_index(drop=True).idxmax()
    return df.iloc[position].to_dict()


def get_lowest_student(df: pd.DataFrame) -> dict:
    """Return the lowest-scoring student."""
    if df.empty:
        raise ValueError("No student records are available.")

    position = df["Final_Marks"].reset_index(drop=True).idxmin()
    return df.iloc[position].to_dict()


def find_top_three_students(df: pd.DataFrame) -> pd.DataFrame:
    """Return the three students with the highest final marks."""
    return (
        df.sort_values(
            by="Final_Marks",
            ascending=False,
            kind="stable",
        )
        .head(3)
        .reset_index(drop=True)
    )


def calculate_pass_percentage(df: pd.DataFrame, pass_mark: float = PASS_MARK) -> float:
    """Calculate the percentage of students who passed."""
    if not 0 <= pass_mark <= 100:
        raise ValueError("Pass mark must be between 0 and 100.")

    if df.empty:
        return 0.0

    passed = (df["Final_Marks"] >= pass_mark).sum()
    return round(float(passed / len(df) * 100), 2)


def compare_previous_and_final_marks(df: pd.DataFrame) -> pd.DataFrame:
    """Compare previous and final marks for each student."""
    result = df[
        ["Student_ID", "Previous_Marks", "Final_Marks"]
    ].copy()

    result["Mark_Change"] = (
        result["Final_Marks"] - result["Previous_Marks"]
    )

    result["Improvement_Status"] = result["Mark_Change"].map(
        lambda value: (
            "Improved" if value > 0
            else "Declined" if value < 0
            else "Unchanged"
        )
    )

    return result


def calculate_average_improvement(df: pd.DataFrame) -> float:
    """Calculate the average change in marks."""
    changes = compare_previous_and_final_marks(df)["Mark_Change"]

    if changes.empty:
        return 0.0

    return round(float(changes.mean()), 2)


def get_improvement_summary(df: pd.DataFrame) -> dict:
    """Summarize improvements, declines, and unchanged marks."""
    changes = compare_previous_and_final_marks(df)["Mark_Change"]

    return {
        "improved_students": int((changes > 0).sum()),
        "declined_students": int((changes < 0).sum()),
        "unchanged_students": int((changes == 0).sum()),
        "average_mark_change": (
            round(float(changes.mean()), 2)
            if not changes.empty
            else 0.0
        ),
    }


def get_performance_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Assign performance categories based on final marks."""
    result = df.copy()

    result["Performance_Category"] = pd.cut(
        result["Final_Marks"],
        bins=PERFORMANCE_BINS,
        labels=PERFORMANCE_LABELS,
        include_lowest=True,
        right=False,
    )

    return result


def get_grade_counts(df: pd.DataFrame) -> dict:
    """Count students in each performance category."""
    categorized = get_performance_categories(df)

    return categorized["Performance_Category"].value_counts(
        sort=False
    ).to_dict()


def get_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate correlations between numerical measures."""
    return df[NUMERIC_COLUMNS].corr().round(2)


def get_descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate descriptive statistics."""
    return df[NUMERIC_COLUMNS].describe().round(2)


def get_attendance_summary(df: pd.DataFrame) -> dict:
    """Summarize attendance using mean and median."""
    attendance = df["Attendance"]

    if attendance.empty:
        return {
            "average_attendance": 0.0,
            "median_attendance": 0.0,
            "low_attendance_students": 0,
        }

    return {
        "average_attendance": round(float(attendance.mean()), 2),
        "median_attendance": round(float(attendance.median()), 2),
        "low_attendance_students": int((attendance < 75).sum()),
    }


def get_study_hours_summary(df: pd.DataFrame) -> dict:
    """Summarize study hours and identify low study time."""
    hours = df["Study_Hours"]

    if hours.empty:
        return {
            "average_study_hours": 0.0,
            "median_study_hours": 0.0,
            "low_study_hours_students": 0,
        }

    return {
        "average_study_hours": round(float(hours.mean()), 2),
        "median_study_hours": round(float(hours.median()), 2),
        "low_study_hours_students": int((hours < 2).sum()),
    }


def get_score_distribution(df: pd.DataFrame) -> dict:
    """Count students within final-mark ranges."""
    marks = df["Final_Marks"]

    return {
        "Below 40": int((marks < 40).sum()),
        "40 to 59": int(((marks >= 40) & (marks < 60)).sum()),
        "60 to 79": int(((marks >= 60) & (marks < 80)).sum()),
        "80 to 100": int(((marks >= 80) & (marks <= 100)).sum()),
    }


def find_students_needing_support(
    df: pd.DataFrame,
    pass_mark: float = PASS_MARK,
) -> pd.DataFrame:
    """Identify students scoring below the pass mark."""
    if not 0 <= pass_mark <= 100:
        raise ValueError("Pass mark must be between 0 and 100.")

    students = df[df["Final_Marks"] < pass_mark].copy()

    students["Support_Reason"] = students["Final_Marks"].map(
        lambda marks: (
            "Needs immediate support"
            if marks < pass_mark / 2
            else "Needs extra practice"
        )
    )

    return students.reset_index(drop=True)


def get_student_performance_summary(df: pd.DataFrame) -> dict:
    """Summarize students using the configured performance categories."""
    required_columns = {
        "Student_ID",
        "Study_Hours",
        "Attendance",
        "Final_Marks",
    }
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if df.empty:
        return {
            "total_students": 0,
            "high_performers": 0,
            "average_performers": 0,
            "low_performers": 0,
            "average_final_marks": 0.0,
        }

    marks = df["Final_Marks"]

    return {
        "total_students": len(df),
        "high_performers": int((marks >= 80).sum()),
        "average_performers": int(
            ((marks >= 40) & (marks < 80)).sum()
        ),
        "low_performers": int((marks < 40).sum()),
        "average_final_marks": round(float(marks.mean()), 2),
    }


def get_student_performance_details(df: pd.DataFrame) -> pd.DataFrame:
    """Return performance, attendance, and study habit details."""
    required_columns = {
        "Student_ID",
        "Study_Hours",
        "Attendance",
        "Final_Marks",
    }
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    result = df[
        ["Student_ID", "Study_Hours", "Attendance", "Final_Marks"]
    ].copy()

    result["Performance_Level"] = result["Final_Marks"].apply(
        lambda marks: (
            "High Performer" if marks >= 80
            else "Average Performer" if marks >= 40
            else "Low Performer"
        )
    )

    result["Attendance_Status"] = result["Attendance"].apply(
        lambda attendance: (
            "Low Attendance" if attendance < 75
            else "Satisfactory Attendance"
        )
    )

    result["Study_Habit"] = result["Study_Hours"].apply(
        lambda hours: (
            "More Study Recommended" if hours < 2
            else "Regular Study"
        )
    )

    return result.sort_values(
        by="Final_Marks",
        ascending=False,
        kind="stable",
    ).reset_index(drop=True)


def generate_insights(df: pd.DataFrame) -> list[str]:
    """Generate readable findings from student records."""
    if df.empty:
        return ["No student records are available for analysis."]

    averages = calculate_averages(df)
    top = get_top_student(df)
    improvement = get_improvement_summary(df)
    attendance = get_attendance_summary(df)
    study = get_study_hours_summary(df)
    distribution = get_score_distribution(df)

    return [
        f"Total students analyzed: {len(df)}",
        f"Average final marks: {averages['Final_Marks']:.2f}",
        f"Average study hours: {study['average_study_hours']:.2f}",
        f"Average attendance: {attendance['average_attendance']:.2f}%",
        f"Pass percentage: {calculate_pass_percentage(df):.2f}%",
        f"Median final marks: {df['Final_Marks'].median():.2f}",
        f"Students who improved: {improvement['improved_students']}",
        f"Students who declined: {improvement['declined_students']}",
        f"Average mark change: {improvement['average_mark_change']:.2f}",
        f"Students below 40 marks: {distribution['Below 40']}",
        (
            "Students below 75% attendance: "
            f"{attendance['low_attendance_students']}"
        ),
        (
            "Students studying under 2 hours: "
            f"{study['low_study_hours_students']}"
        ),
        (
            f"Highest scorer: Student {int(top['Student_ID'])}, "
            f"{top['Final_Marks']:.0f} marks"
        ),
    ]
