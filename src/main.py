"""Main program for Student Performance Analysis."""

from data import create_student_dataset
from validation import (
    validate_dataset,
    generate_data_quality_summary,
)
from analysis import (
    calculate_averages,
    find_top_and_lowest_students,
    add_performance_category,
    calculate_category_statistics,
    calculate_correlation,
    determine_class_performance,
    find_students_needing_improvement,
    calculate_performance_statistics,
    calculate_pass_percentage,
)
from grade_summary import (
    create_grade_summary,
    save_grade_summary,
    save_student_grades,
)
from report import generate_report
from visualization import (
    create_all_visualizations,
    plot_grade_distribution,
)


def display_performance_summary(
    df, averages, class_level, pass_percentage
):
    """Display the final summary of student performance."""

    students_needing_improvement = (
        df["Performance_Category"] == "Needs Improvement"
    ).sum()

    print("\n" + "=" * 55)
    print("             PERFORMANCE SUMMARY")
    print("=" * 55)
    print(f"Total Students                : {len(df)}")
    print(f"Average Final Marks           : {averages['average_final']:.2f}")
    print(f"Highest Final Marks           : {df['Final_Marks'].max()}")
    print(f"Lowest Final Marks            : {df['Final_Marks'].min()}")
    print(f"Pass Percentage               : {pass_percentage:.2f}%")
    print(
        f"Students Needing Improvement : "
        f"{students_needing_improvement}"
    )
    print(f"Overall Class Performance     : {class_level}")


def display_statistical_analysis(statistics):
    """Display additional statistical measures for final marks."""

    print("\n[10] ADDITIONAL STATISTICAL ANALYSIS")
    print("-" * 55)
    print(f"Median Final Marks            : {statistics['median_final']:.2f}")
    print(f"Standard Deviation            : {statistics['std_final']:.2f}")
    print(f"Minimum Final Marks           : {statistics['minimum_final']:.2f}")
    print(f"Maximum Final Marks           : {statistics['maximum_final']:.2f}")


def display_grade_summary(grade_counts):
    """Display the number of students in each grade."""

    print("\n[11] GRADE SUMMARY")
    print("-" * 55)

    total_students = grade_counts.sum()

    for grade, count in grade_counts.items():
        percentage = (
            count / total_students * 100
            if total_students > 0
            else 0
        )
        print(
            f"Grade {grade:<15}: {count} student(s) "
            f"({percentage:.1f}%)"
        )


def display_data_quality_summary(summary):
    """Display the results of dataset quality checks."""

    print("\n[2.1] DATA QUALITY SUMMARY")
    print("-" * 55)
    print(f"Total Rows             : {summary['total_rows']}")
    print(f"Total Columns          : {summary['total_columns']}")
    print(f"Missing Values         : {summary['missing_values']}")
    print(f"Duplicate Student IDs  : {summary['duplicate_student_ids']}")
    print(f"Data Quality Status    : {summary['data_quality_status']}")


def display_completion_summary():
    """Display a message confirming successful analysis completion."""

    print("\n" + "=" * 55)
    print("             ANALYSIS COMPLETED")
    print("=" * 55)
    print("Dataset validation completed.")
    print("Dataset processed successfully.")
    print("Statistical analysis completed.")
    print("Performance classification completed.")
    print("Grade classification completed.")
    print("Correlation analysis completed.")
    print("Pass percentage calculated.")
    print("Visualizations generated.")
    print("CSV files exported.")
    print("Text report generated.")
    print("Final performance summary generated.")
    print("=" * 55)


def main():
    """Run the complete student performance analysis."""

    # 1. Create the student dataset
    df = create_student_dataset()

    # 2. Validate the dataset
    validate_dataset(df)

    print("\n" + "=" * 55)
    print("          STUDENT PERFORMANCE ANALYSIS")
    print("=" * 55)

    # 3. Display the dataset
    print("\n[1] STUDENT DATASET")
    print("-" * 55)
    print(df)

    # 4. Display dataset statistics
    print("\n[2] DATASET SUMMARY")
    print("-" * 55)
    print(df.describe())

    # 5. Display data quality information
    quality_summary = generate_data_quality_summary(df)
    display_data_quality_summary(quality_summary)

    # 6. Calculate average performance
    averages = calculate_averages(df)

    print("\n[3] AVERAGE PERFORMANCE")
    print("-" * 55)
    print(f"Average Final Marks       : {averages['average_final']:.2f}")
    print(f"Average Study Hours       : {averages['average_study']:.2f}")
    print(
        f"Average Attendance        : "
        f"{averages['average_attendance']:.2f}%"
    )
    print(
        f"Average Assignment Score  : "
        f"{averages['average_assignment']:.2f}"
    )

    # 7. Find highest and lowest performing students
    highest_student, lowest_student = find_top_and_lowest_students(df)

    print("\n[4] HIGHEST PERFORMING STUDENT")
    print("-" * 55)
    print(highest_student)

    print("\n[5] LOWEST PERFORMING STUDENT")
    print("-" * 55)
    print(lowest_student)

    # 8. Add performance categories
    df = add_performance_category(df)

    print("\n[6] PERFORMANCE CATEGORIES")
    print("-" * 55)
    print(
        df[
            ["Student_ID", "Final_Marks", "Performance_Category"]
        ]
    )

    # 9. Find students needing improvement
    students_needing_improvement = find_students_needing_improvement(df)

    print("\n[6.1] STUDENTS NEEDING IMPROVEMENT")
    print("-" * 55)
    print(students_needing_improvement)

    # 10. Calculate category statistics
    category_counts, category_percentages = (
        calculate_category_statistics(df)
    )

    print("\n[7] CATEGORY STATISTICS")
    print("-" * 55)
    print("Category Count:")
    print(category_counts)

    print("\nCategory Percentages:")
    for category, percentage in category_percentages.items():
        print(f"{category:<20}: {percentage:.1f}%")

    # 11. Calculate correlations
    print("\n[8] CORRELATION WITH FINAL MARKS")
    print("-" * 55)
    print(calculate_correlation(df))

    # 12. Add grades and calculate grade summary
    df, grade_counts = create_grade_summary(df)
    display_grade_summary(grade_counts)

    # 13. Generate visualizations
    print("\n[9] GENERATING VISUALIZATIONS")
    print("-" * 55)
    create_all_visualizations(df)
    plot_grade_distribution(df)

    # 14. Calculate additional statistics
    performance_statistics = calculate_performance_statistics(df)
    display_statistical_analysis(performance_statistics)

    # 15. Calculate pass percentage
    pass_percentage = calculate_pass_percentage(df)

    # 16. Determine overall class performance
    class_level = determine_class_performance(
        averages["average_final"]
    )

    # 17. Display final performance summary
    display_performance_summary(
        df,
        averages,
        class_level,
        pass_percentage,
    )

    # 18. Export grade summaries
    grade_summary_file = save_grade_summary(
        grade_counts,
        "grade_summary.csv",
    )
    student_grades_file = save_student_grades(
        df,
        "student_grades.csv",
    )

    # 19. Generate text report
    report_file = generate_report(
        df,
        "student_performance_report.txt",
    )

    print("\n[12] GENERATED FILES")
    print("-" * 55)
    print(f"Grade Summary CSV       : {grade_summary_file}")
    print(f"Student Grades CSV      : {student_grades_file}")
    print(f"Performance Report      : {report_file}")

    # 20. Display completion message
    display_completion_summary()


if __name__ == "__main__":
    main()