
import pandas as pd

PASS_MARK = 40

PERFORMANCE_BINS = [-1, 39, 59, 79, 100]
PERFORMANCE_LABELS = [
    "Needs Improvement",
    "Satisfactory",
    "Good",
    "Excellent",
]

NUMERIC_COLUMNS = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Final_Marks",
]


def calculate_averages(df):
    """Calculate average values for student performance."""
    return df[NUMERIC_COLUMNS].mean().round(2).to_dict()


def get_top_student(df):
    """Return the student with the highest final marks."""
    if df.empty:
        raise ValueError("Cannot find a top student in an empty dataset.")

    return df.loc[df["Final_Marks"].idxmax()].to_dict()


def get_lowest_student(df):
    """Return the student with the lowest final marks."""
    if df.empty:
        raise ValueError("Cannot find a lowest-scoring student in an empty dataset.")

    return df.loc[df["Final_Marks"].idxmin()].to_dict()


def find_top_three_students(df):
    """Return the three students with the highest final marks."""
    return (
        df.nlargest(3, "Final_Marks")
        .reset_index(drop=True)
    )


def calculate_pass_percentage(df, pass_mark=PASS_MARK):
    """Calculate the percentage of students who passed."""
    if not 0 <= pass_mark <= 100:
        raise ValueError("Pass mark must be between 0 and 100.")

    if df.empty:
        return 0.0

    passed = (df["Final_Marks"] >= pass_mark).sum()
    return round(float(passed / len(df) * 100), 2)


def calculate_average_improvement(df):
    """Calculate the average change in student marks."""
    change = df["Final_Marks"] - df["Previous_Marks"]

    if change.empty:
        return 0.0

    return round(float(change.mean()), 2)


def get_performance_categories(df):
    """Assign a performance category to every student."""
    result = df.copy()

    result["Performance_Category"] = pd.cut(
        result["Final_Marks"],
        bins=PERFORMANCE_BINS,
        labels=PERFORMANCE_LABELS,
    )

    return result


def get_grade_counts(df):
    """Count students in each performance category."""
    categorized = get_performance_categories(df)

    return categorized["Performance_Category"].value_counts(
        sort=False
    ).to_dict()


def get_correlation_matrix(df):
    """Calculate correlations between numerical performance measures."""
    return df[NUMERIC_COLUMNS].corr().round(2)


def get_descriptive_statistics(df):
    """Return descriptive statistics for numerical columns."""
    return df[NUMERIC_COLUMNS].describe().round(2)


def compare_previous_and_final_marks(df):
    """Compare previous marks with final marks for each student."""
    result = df[
        ["Student_ID", "Previous_Marks", "Final_Marks"]
    ].copy()

    result["Mark_Change"] = (
        result["Final_Marks"] - result["Previous_Marks"]
    )

    result["Improvement_Status"] = result["Mark_Change"].apply(
        lambda value: (
            "Improved" if value > 0
            else "Declined" if value < 0
            else "Unchanged"
        )
    )

    return result


def get_improvement_summary(df):
    """Summarize student improvement and decline."""
    comparison = compare_previous_and_final_marks(df)
    changes = comparison["Mark_Change"]

    return {
        "improved_students": int((changes > 0).sum()),
        "declined_students": int((changes < 0).sum()),
        "unchanged_students": int((changes == 0).sum()),
        "average_mark_change": (
            round(float(changes.mean()), 2)
            if not changes.empty else 0.0
        ),
    }


def find_students_needing_support(df, pass_mark=PASS_MARK):
    """Find students scoring below the pass mark."""
    required_columns = {"Student_ID", "Final_Marks"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    if not 0 <= pass_mark <= 100:
        raise ValueError("Pass mark must be between 0 and 100.")

    students = df[df["Final_Marks"] < pass_mark].copy()

    students["Support_Reason"] = students["Final_Marks"].apply(
        lambda marks: (
            "Needs immediate support"
            if marks < pass_mark / 2
            else "Needs extra practice"
        )
    )

    return students.reset_index(drop=True)


def get_attendance_summary(df):
    """Summarize attendance across students."""
    attendance = df["Attendance"]

    if attendance.empty:
        return {
            "average_attendance": 0.0,
            "highest_attendance": 0.0,
            "lowest_attendance": 0.0,
            "low_attendance_students": 0,
        }

    return {
        "average_attendance": round(float(attendance.mean()), 2),
        "highest_attendance": round(float(attendance.max()), 2),
        "lowest_attendance": round(float(attendance.min()), 2),
        "low_attendance_students": int((attendance < 75).sum()),
    }


def generate_insights(df):
    """Generate simple insights from the student dataset."""
    if df.empty:
        return ["No student records are available for analysis."]

    averages = calculate_averages(df)
    top = get_top_student(df)
    improvement = get_improvement_summary(df)
    attendance = get_attendance_summary(df)

    return [
        f"Students analyzed: {len(df)}",
        f"Average final marks: {averages['Final_Marks']:.2f}",
        f"Average study hours: {averages['Study_Hours']:.2f}",
        f"Average attendance: {averages['Attendance']:.2f}%",
        f"Pass percentage: {calculate_pass_percentage(df):.2f}%",
        f"Students who improved: {improvement['improved_students']}",
        f"Students who declined: {improvement['declined_students']}",
        f"Average mark change: {improvement['average_mark_change']:.2f}",
        f"Students with attendance below 75%: {attendance['low_attendance_students']}",
        (
            f"Highest scorer: Student {int(top['Student_ID'])}, "
            f"{top['Final_Marks']:.0f} marks"
        ),
    ]
