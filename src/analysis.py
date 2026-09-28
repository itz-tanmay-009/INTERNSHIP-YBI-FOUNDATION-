"""Functions for analyzing student academic performance."""

from validation import MINIMUM_PASSING_MARKS


def calculate_averages(df):
    """Calculate average values for key student performance metrics."""
    return {
        "average_final": df["Final_Marks"].mean(),
        "average_study": df["Study_Hours"].mean(),
        "average_attendance": df["Attendance"].mean(),
        "average_assignment": df["Assignment_Score"].mean()
    }


def find_top_and_lowest_students(df):
    """Find the students with the highest and lowest final marks."""
    highest_student = df.loc[df["Final_Marks"].idxmax()]
    lowest_student = df.loc[df["Final_Marks"].idxmin()]

    return highest_student, lowest_student


def performance_category(marks):
    """Classify a student's performance based on final marks."""
    if marks >= 85:
        return "Excellent"
    if marks >= 70:
        return "Good"
    return "Needs Improvement"


def add_performance_category(df):
    """Add a performance category column to the DataFrame."""
    df["Performance_Category"] = df["Final_Marks"].apply(
        performance_category
    )
    return df


def calculate_category_statistics(df):
    """Calculate counts and percentages for each performance category."""
    category_counts = df["Performance_Category"].value_counts()

    category_percentages = (
        df["Performance_Category"]
        .value_counts(normalize=True)
        .mul(100)
    )

    return category_counts, category_percentages


def calculate_correlation(df):
    """Calculate correlations between academic factors and final marks."""
    columns = [
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    ]

    return df[columns].corr()["Final_Marks"]


def determine_class_performance(average_final):
    """Determine overall class performance from average final marks."""
    if average_final >= 85:
        return "Excellent"
    if average_final >= 70:
        return "Good"
    return "Needs Improvement"


def find_students_needing_improvement(df):
    """Return students whose final marks are below 70."""
    return df[df["Final_Marks"] < 70][
        ["Student_ID", "Final_Marks"]
    ]


def calculate_performance_statistics(df):
    """Calculate additional statistical measures for final marks."""
    return {
        "median_final": df["Final_Marks"].median(),
        "std_final": df["Final_Marks"].std(),
        "minimum_final": df["Final_Marks"].min(),
        "maximum_final": df["Final_Marks"].max()
    }


def calculate_pass_percentage(df):
    """Calculate the percentage of students who meet the passing mark."""
    total_students = len(df)

    if total_students == 0:
        return 0.0

    passed_students = (
        df["Final_Marks"] >= MINIMUM_PASSING_MARKS
    ).sum()

    return (passed_students / total_students) * 100