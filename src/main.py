from pathlib import Path

from data import load_data
from validation import validate_data, get_data_quality_summary

from analysis import (
    calculate_averages,
    calculate_pass_percentage,
    get_top_student,
    find_top_three_students,
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
    """Run the complete student performance analysis."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("STUDENT PERFORMANCE ANALYSIS")
    print("=" * 60)

    df = load_data()

    validate_data(df)
    quality = get_data_quality_summary(df)

    print("\nDATA QUALITY")
    print(f"Total rows: {quality['total_rows']}")
    print(f"Total columns: {quality['total_columns']}")
    print(f"Missing values: {quality['missing_values']}")
    print(f"Duplicate rows: {quality['duplicate_rows']}")

    print("\nAVERAGE STATISTICS")

    averages = calculate_averages(df)

    for name, value in averages.items():
        suffix = "%" if name == "Attendance" else ""
        print(f"{name}: {value:.2f}{suffix}")

    print(
        f"\nPass percentage: "
        f"{calculate_pass_percentage(df):.2f}%"
    )

    top = get_top_student(df)
    print(
        f"Highest scorer: Student {int(top['Student_ID'])}, "
        f"{top['Final_Marks']:.0f} marks"
    )

    print("\nTOP THREE STUDENTS")
    print(find_top_three_students(df).to_string(index=False))

    print("\nIMPROVEMENT SUMMARY")

    improvement = get_improvement_summary(df)

    for name, value in improvement.items():
        print(f"{name.replace('_', ' ').title()}: {value}")

    save_all_grade_summaries(df, OUTPUT_DIR)

    get_descriptive_statistics(df).to_csv(
        OUTPUT_DIR / "descriptive_statistics.csv"
    )

    get_correlation_matrix(df).to_csv(
        OUTPUT_DIR / "correlation_matrix.csv"
    )

    chart_paths = create_all_charts(
        df,
        OUTPUT_DIR / "charts",
    )

    report_text = generate_report(df)

    report_path = save_report(
        report_text,
        OUTPUT_DIR / "student_performance_report.txt",
    )

    print("\nFILES GENERATED")
    print(f"Report: {report_path}")
    print(f"Charts generated: {len(chart_paths)}")
    print(f"Output folder: {OUTPUT_DIR}")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, FileNotFoundError) as error:
        print(f"\nError: {error}")
        raise SystemExit(1)