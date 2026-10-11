import pandas as pd

PASS_MARK = 40


def calculate_averages(df):
    columns = [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Marks",
        "Final_Marks",
    ]
    return df[columns].mean().round(2).to_dict()


def get_top_student(df):
    return df.loc[df["Final_Marks"].idxmax()].to_dict()


def get_lowest_student(df):
    return df.loc[df["Final_Marks"].idxmin()].to_dict()


def find_top_three_students(df):
    return df.nlargest(3, "Final_Marks").reset_index(drop=True)


def calculate_pass_percentage(df, pass_mark=PASS_MARK):
    if df.empty:
        return 0.0
    passed = (df["Final_Marks"] >= pass_mark).sum()
    return round(float(passed / len(df) * 100), 2)


def calculate_average_improvement(df):
    difference = df["Final_Marks"] - df["Previous_Marks"]
    return round(float(difference.mean()), 2)


def get_performance_categories(df):
    result = df.copy()
    result["Performance_Category"] = pd.cut(
        result["Final_Marks"],
        bins=[-1, 39, 59, 79, 100],
        labels=[
            "Needs Improvement",
            "Satisfactory",
            "Good",
            "Excellent",
        ],
    )
    return result


def get_grade_counts(df):
    categorized = get_performance_categories(df)
    return categorized["Performance_Category"].value_counts(
        sort=False
    ).to_dict()


def get_correlation_matrix(df):
    columns = [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Marks",
        "Final_Marks",
    ]
    return df[columns].corr().round(2)


def get_descriptive_statistics(df):
    columns = [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Marks",
        "Final_Marks",
    ]
    return df[columns].describe().round(2)


def generate_insights(df):
    averages = calculate_averages(df)
    top = get_top_student(df)

    return [
        f"Average final marks: {averages['Final_Marks']:.2f}",
        f"Average study hours: {averages['Study_Hours']:.2f}",
        f"Average attendance: {averages['Attendance']:.2f}%",
        f"Pass percentage: {calculate_pass_percentage(df):.2f}%",
        f"Average mark improvement: {calculate_average_improvement(df):.2f}",
        (
            f"Highest scorer: Student {int(top['Student_ID'])} "
            f"with {top['Final_Marks']:.0f} marks"
        ),
    ]