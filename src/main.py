
from pathlib import Path

from data import load_data
from validation import validate_data, get_data_quality_summary

from analysis import (
    calculate_averages,
    calculate_pass_percentage,
    find_top_three_students,
    find_students_needing_support,
    get_descriptive_statistics,
    get_correlation_matrix,
    get_improvement_summary,
)

from grade_summary import save_all_grade_summaries
from visualization import create_all_charts
from report import generate_report, save_report


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"


def main():
    """Run the complete student performance analysis project."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 55)
    print("STUDENT PERFORMANCE ANALYSIS")
    print("=" * 55)

    df = load_data()

    validate_data(df)
    quality = get_data_quality_summary(df)

    print("\nDATA QUALITY SUMMARY")
    print("-" * 35)
    print(f"Total records: {quality['total_rows']}")
    print(f"Total columns: {quality['total_columns']}")
    print(f"Missing values: {quality['missing_values']}")
    print(f"Duplicate rows: {quality['duplicate_rows']}")

    print("\nAVERAGE PERFORMANCE")
    print("-" * 35)

    averages = calculate_averages(df)

    for column, value in averages.items():
        suffix = "%" if column == "Attendance" else ""
        print(f"{column}: {value:.2f}{suffix}")

    print(
        "\nPass percentage: "
        f"{calculate_pass_percentage(df):.2f}%"
    )

    print("\nTOP THREE STUDENTS")
    print("-" * 35)
    print(find_top_three_students(df).to_string(index=False))

    print("\nIMPROVEMENT SUMMARY")
    print("-" * 35)

    improvement = get_improvement_summary(df)

    for name, value in improvement.items():
        print(f"{name.replace('_', ' ').title()}: {value}")

    print("\nSTUDENTS NEEDING SUPPORT")
    print("-" * 35)

    support_students = find_students_needing_support(df)

    if support_students.empty:
        print("No students scored below the pass mark.")
    else:
        print(support_students.to_string(index=False))
        support_students.to_csv(
            OUTPUT_DIR / "students_needing_support.csv",
            index=False,
        )

    print("\nGENERATING OUTPUT FILES")
    print("-" * 35)

    save_all_grade_summaries(df, OUTPUT_DIR)

    statistics_path = OUTPUT_DIR / "descriptive_statistics.csv"
    get_descriptive_statistics(df).to_csv(statistics_path)

    correlation_path = OUTPUT_DIR / "correlation_matrix.csv"
    get_correlation_matrix(df).to_csv(correlation_path)

    chart_paths = create_all_charts(
        df,
        OUTPUT_DIR / "charts",
    )

    report_path = save_report(
        generate_report(df),
        OUTPUT_DIR / "student_performance_report.txt",
    )

    print(f"Grade summaries saved in: {OUTPUT_DIR}")
    print(f"Statistics saved in: {statistics_path}")
    print(f"Correlation matrix saved in: {correlation_path}")
    print(f"Charts generated: {len(chart_paths)}")
    print(f"Report saved in: {report_path}")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"\nProject error: {error}")
        raise SystemExit(1)
