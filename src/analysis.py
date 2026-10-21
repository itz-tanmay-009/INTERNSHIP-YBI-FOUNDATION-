
import pandas as pd


PASS_MARK = 40

NUMERIC_COLUMNS = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]

PERFORMANCE_BINS = [-0.001, 39, 59, 79, 100]
PERFORMANCE_LABELS = [
    "Needs Improvement",
    "Satisfactory",
    "Good",
    "Excellent",
]


def calculate_averages(df):
    """Calculate averages for numerical columns."""
    return df[NUMERIC_COLUMNS].mean().round(2).to_dict()


def get_top_student(df):
    """Find the student with the highest final marks."""
    if df.empty:
        raise ValueError("No student records are available.")
    return df.loc[df["Final_Marks"].idxmax()].to_dict()


def get_lowest_student(df):
    """Find the student with the lowest final marks."""
    if df.empty:
        raise ValueError("No student records are available.")
    return df.loc[df["Final_Marks"].idxmin()].to_dict()


def find_top_three_students(df):
    """Return the three students with the highest final marks."""
    return df.nlargest(3, "Final_Marks").reset_index(drop=True)


def calculate_pass_percentage(df, pass_mark=PASS_MARK):
    """Calculate the percentage of students who passed."""
    if not 0 <= pass_mark <= 100:
        raise ValueError("Pass mark must be between 0 and 100.")
    if df.empty:
        return 0.0

    passed = (df["Final_Marks"] >= pass_mark).sum()
    return round(float(passed / len(df) * 100), 2)


def compare_previous_and_final_marks(df):
    """Compare previous and final marks."""
    result = df[
        ["Student_ID", "Previous_Marks", "Final_Marks"]
    ].copy()

    result["Mark_Change"] = (
        result["Final_Marks"] - result["Previous_Marks"]
    )

    result["Improvement_Status"] = result["Mark_Change"].map(
        lambda change: (
            "Improved" if change > 0
            else "Declined" if change < 0
            else "Unchanged"
        )
    )

    return result


def calculate_average_improvement(df):
    """Calculate the average change in marks."""
    changes = compare_previous_and_final_marks(df)["Mark_Change"]

    if changes.empty:
        return 0.0

    return round(float(changes.mean()), 2)


def get_improvement_summary(df):
    """Summarize improvements, declines, and unchanged marks."""
    changes = compare_previous_and_final_marks(df)["Mark_Change"]

    return {
        "improved_students": int((changes > 0).sum()),
        "declined_students": int((changes < 0).sum()),
        "unchanged_students": int((changes == 0).sum()),
        "average_mark_change": (
            round(float(changes.mean()), 2)
            if not changes.empty else 0.0
        ),
    }


def get_performance_categories(df):
    """Assign a performance category based on final marks."""
    result = df.copy()

    result["Performance_Category"] = pd.cut(
        result["Final_Marks"],
        bins=PERFORMANCE_BINS,
        labels=PERFORMANCE_LABELS,
        include_lowest=True,
    )

    return result


def get_grade_counts(df):
    """Count students in each performance category."""
    categorized = get_performance_categories(df)
    return categorized["Performance_Category"].value_counts(
        sort=False
    ).to_dict()


def get_correlation_matrix(df):
    """Calculate correlations between numerical measures."""
    return df[NUMERIC_COLUMNS].corr().round(2)


def get_descriptive_statistics(df):
    """Calculate descriptive statistics."""
    return df[NUMERIC_COLUMNS].describe().round(2)


def get_attendance_summary(df):
    """Summarize student attendance."""
    attendance = df["Attendance"]

    if attendance.empty:
        return {
            "average_attendance": 0.0,
            "low_attendance_students": 0,
        }

    return {
        "average_attendance": round(float(attendance.mean()), 2),
        "low_attendance_students": int((attendance < 75).sum()),
    }


def get_study_hours_summary(df):
    """Summarize study hour patterns in the dataset."""
    study_hours = df["Study_Hours"]

    if study_hours.empty:
        return {
            "average_study_hours": 0.0,
            "low_study_hours_students": 0,
        }

    return {
        "average_study_hours": round(float(study_hours.mean()), 2),
        "low_study_hours_students": int((study_hours < 2).sum()),
    }


def find_students_needing_support(df, pass_mark=PASS_MARK):
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


def get_student_performance_summary(df):
    """Summarize students by performance level."""
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
        "average_performers": int(((marks >= 50) & (marks < 80)).sum()),
        "low_performers": int((marks < 50).sum()),
        "average_final_marks": round(float(marks.mean()), 2),
    }


def get_student_performance_details(df):
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
            else "Average Performer" if marks >= 50
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
    ).reset_index(drop=True)


def generate_insights(df):
    """Generate readable findings from student records."""
    if df.empty:
        return ["No student records are available for analysis."]

    averages = calculate_averages(df)
    top = get_top_student(df)
    improvement = get_improvement_summary(df)
    attendance = get_attendance_summary(df)
    study = get_study_hours_summary(df)

    return [
        f"Total students analyzed: {len(df)}",
        f"Average final marks: {averages['Final_Marks']:.2f}",
        f"Average study hours: {study['average_study_hours']:.2f}",
        f"Average attendance: {attendance['average_attendance']:.2f}%",
        f"Pass percentage: {calculate_pass_percentage(df):.2f}%",
        f"Students who improved: {improvement['improved_students']}",
        f"Students who declined: {improvement['declined_students']}",
        f"Average mark change: {improvement['average_mark_change']:.2f}",
        (
            "Students with attendance below 75%: "
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
