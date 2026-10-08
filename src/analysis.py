"""Functions for analyzing student academic performance."""

from validation import MINIMUM_PASSING_MARKS


def calculate_averages(df):
    """Calculate average values for key student performance metrics."""

    columns = {
        "average_final": "Final_Marks",
        "average_study": "Study_Hours",
        "average_attendance": "Attendance",
        "average_assignment": "Assignment_Score"
    }

    return {
        result_name: df[column_name].mean()
        for result_name, column_name in columns.items()
    }


def find_top_and_lowest_students(df):
    """Find the students with the highest and lowest final marks."""

    marks = df["Final_Marks"]

    highest_student = df.loc[marks.idxmax()]
    lowest_student = df.loc[marks.idxmin()]

    return highest_student, lowest_student


def performance_category(marks):
    """Classify a student's performance based on final marks."""

    categories = [
        (85, "Excellent"),
        (70, "Good")
    ]

    for minimum_marks, category in categories:
        if marks >= minimum_marks:
            return category

    return "Needs Improvement"


def add_performance_category(df):
    """Add a performance category column to the DataFrame."""

    df["Performance_Category"] = df["Final_Marks"].map(
        performance_category
    )

    return df


def calculate_category_statistics(df):
    """Calculate counts and percentages for each performance category."""

    category_counts = df["Performance_Category"].value_counts()
    category_percentages = category_counts.div(len(df)).mul(100)

    return category_counts, category_percentages


def calculate_correlation(df):
    """Calculate correlations between academic factors and final marks."""

    academic_columns = [
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    ]

    correlation_matrix = df[academic_columns].corr()

    return correlation_matrix["Final_Marks"]


def determine_class_performance(average_final):
    """Determine overall class performance from average final marks."""

    return performance_category(average_final)


def find_students_needing_improvement(df):
    """Return students whose final marks are below 70."""

    needs_improvement = df["Final_Marks"] < 70

    return df.loc[
        needs_improvement,
        ["Student_ID", "Final_Marks"]
    ]


def calculate_performance_statistics(df):
    """Calculate additional statistical measures for final marks."""

    final_marks = df["Final_Marks"]

    return {
        "median_final": final_marks.median(),
        "std_final": final_marks.std(),
        "minimum_final": final_marks.min(),
        "maximum_final": final_marks.max()
    }


def calculate_average_improvement(df):
    """Calculate the average improvement from previous to final marks."""

    if df.empty:
        return 0.0

    improvement = df["Final_Marks"] - df["Previous_Marks"]

    return improvement.mean()


def calculate_pass_percentage(df):
    """Calculate the percentage of students who meet the passing mark."""

    if df.empty:
        return 0.0

    passed_count = df["Final_Marks"].ge(
        MINIMUM_PASSING_MARKS
    ).sum()

    return passed_count / len(df) * 100


def calculate_pass_fail_count(df):
    """Return the number of students who passed and failed."""

    passed_count = df["Final_Marks"].ge(
        MINIMUM_PASSING_MARKS
    ).sum()

    failed_count = len(df) - passed_count

    return passed_count, failed_count