
from pathlib import Path

from analysis import (
    get_performance_categories,
    compare_previous_and_final_marks,
)


def create_grade_summary(df):
    """Create student-level and category-level summaries."""
    categorized = get_performance_categories(df)

    summary = categorized[
        [
            "Student_ID",
            "Previous_Marks",
            "Assignment_Marks",
            "Final_Marks",
            "Performance_Category",
        ]
    ].copy()

    comparison = compare_previous_and_final_marks(df)

    summary = summary.merge(
        comparison[
            ["Student_ID", "Mark_Change", "Improvement_Status"]
        ],
        on="Student_ID",
        how="left",
        validate="one_to_one",
    )

    groups = summary.groupby("Performance_Category", observed=False)

    counts = groups.size().rename("Student_Count").reset_index()

    averages = (
        groups["Final_Marks"]
        .mean()
        .round(2)
        .rename("Average_Final_Marks")
        .reset_index()
    )

    return summary, counts, averages


def save_grade_summary(
    summary,
    average_marks=None,
    output_file="output/grade_summary.csv",
):
    """Save a summary DataFrame as a CSV file."""
    if isinstance(average_marks, (str, Path)):
        output_file = average_marks

    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(path, index=False)

    return path


def save_all_grade_summaries(df, output_dir="output"):
    """Save student summaries and category statistics."""
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    summary, counts, averages = create_grade_summary(df)

    paths = {
        "summary": directory / "grade_summary.csv",
        "counts": directory / "grade_counts.csv",
        "averages": directory / "grade_average_marks.csv",
    }

    summary.to_csv(paths["summary"], index=False)
    counts.to_csv(paths["counts"], index=False)
    averages.to_csv(paths["averages"], index=False)

    return paths
