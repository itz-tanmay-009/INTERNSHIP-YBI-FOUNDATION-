from pathlib import Path

from analysis import (
    calculate_averages,
    calculate_pass_percentage,
    find_top_three_students,
    get_correlation_matrix,
    get_descriptive_statistics,
    get_top_student,
)
from data import load_data
from grade_summary import create_grade_summary, save_grade_summary
from report import generate_report, save_report
from validation import validate_data, get_data_quality_summary
from visualization import create_all_charts

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("STUDENT PERFORMANCE ANALYSIS")
    print("=" * 60)

    df = load_data()
    validate_data(df)

    quality = get_data_quality_summary(df)

    print("\nDATA QUALITY")
    print(f"Rows: {quality['rows']}")
    print(f"Columns: {quality['columns']}")
    print(f"Missing values: {quality['missing_values']}")

    print("\nAVERAGE STATISTICS")
    for metric, value in calculate_averages(df).items():
        suffix = "%" if metric == "Attendance" else ""
        print(f"{metric}: {value:.2f}{suffix}")

    print(f"\nPass percentage: {calculate_pass_percentage(df):.2f}%")

    top = get_top_student(df)
    print(
        f"Highest scorer: Student {int(top['Student_ID'])}, "
        f"{top['Final_Marks']:.0f} marks"
    )

    print("\nTOP THREE STUDENTS")
    print(find_top_three_students(df).to_string(index=False))

    summary, counts, averages = create_grade_summary(df)

    save_grade_summary(
        summary,
        output_file=OUTPUT_DIR / "grade_summary.csv",
    )
    counts.to_csv(OUTPUT_DIR / "grade_counts.csv", index=False)
    averages.to_csv(
        OUTPUT_DIR / "grade_average_marks.csv",
        index=False,
    )

    get_descriptive_statistics(df).to_csv(
        OUTPUT_DIR / "descriptive_statistics.csv"
    )
    get_correlation_matrix(df).to_csv(
        OUTPUT_DIR / "correlation_matrix.csv"
    )

    chart_paths = create_all_charts(
        df,
        output_dir=OUTPUT_DIR / "charts",
    )

    report_path = save_report(
        generate_report(df),
        OUTPUT_DIR / "student_performance_report.txt",
    )

    print("\nOUTPUTS")
    print(f"Report: {report_path}")
    print(f"Charts generated: {len(chart_paths)}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print(f"\nAnalysis failed: {error}")
        raise SystemExit(1)