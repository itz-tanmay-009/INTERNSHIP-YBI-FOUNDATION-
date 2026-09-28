from data import create_student_dataset
from validation import validate_dataset
from analysis import (
    calculate_averages,
    find_top_and_lowest_students,
    add_performance_category,
    calculate_category_statistics,
    calculate_correlation,
    determine_class_performance,
    find_students_needing_improvement,
    calculate_performance_statistics,
    calculate_pass_percentage
)
from visualization import create_all_visualizations


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
    print(
        f"Median Final Marks            : "
        f"{statistics['median_final']:.2f}"
    )
    print(
        f"Standard Deviation            : "
        f"{statistics['std_final']:.2f}"
    )
    print(
        f"Minimum Final Marks           : "
        f"{statistics['minimum_final']:.2f}"
    )
    print(
        f"Maximum Final Marks           : "
        f"{statistics['maximum_final']:.2f}"
    )


def display_completion_summary():
    """Display a message confirming successful analysis completion."""

    print("\n" + "=" * 55)
    print("             ANALYSIS COMPLETED")
    print("=" * 55)
    print("Dataset validation completed.")
    print("Dataset processed successfully.")
    print("Statistical analysis completed.")
    print("Performance classification completed.")
    print("Correlation analysis completed.")
    print("Pass percentage calculated.")
    print("Visualizations generated.")
    print("Final performance summary generated.")
    print("=" * 55)


def main():
    """Run the complete student performance analysis."""

    # Create the student dataset
    df = create_student_dataset()

    # Validate the dataset before analysis
    validate_dataset(df)

    print("\n" + "=" * 55)
    print("          STUDENT PERFORMANCE ANALYSIS")
    print("=" * 55)

    # Display the dataset
    print("\n[1] STUDENT DATASET")
    print("-" * 55)
    print(df)

    # Display statistical summary
    print("\n[2] DATASET SUMMARY")
    print("-" * 55)
    print(df.describe())

    # Calculate average performance
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

    # Find highest and lowest performing students
    highest_student, lowest_student = find_top_and_lowest_students(df)

    print("\n[4] HIGHEST PERFORMING STUDENT")
    print("-" * 55)
    print(highest_student)

    print("\n[5] LOWEST PERFORMING STUDENT")
    print("-" * 55)
    print(lowest_student)

    # Add performance categories
    df = add_performance_category(df)

    print("\n[6] PERFORMANCE CATEGORIES")
    print("-" * 55)
    print(
        df[
            ["Student_ID", "Final_Marks", "Performance_Category"]
        ]
    )

    # Find students needing improvement
    students_needing_improvement = find_students_needing_improvement(df)

    print("\n[6.1] STUDENTS NEEDING IMPROVEMENT")
    print("-" * 55)
    print(students_needing_improvement)

    # Calculate category statistics
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

    # Calculate correlations
    print("\n[8] CORRELATION WITH FINAL MARKS")
    print("-" * 55)
    print(calculate_correlation(df))

    # Generate visualizations
    print("\n[9] GENERATING VISUALIZATIONS")
    print("-" * 55)
    create_all_visualizations(df)

    # Calculate additional statistics
    performance_statistics = calculate_performance_statistics(df)

    # Display additional statistics
    display_statistical_analysis(performance_statistics)

    # Calculate pass percentage
    pass_percentage = calculate_pass_percentage(df)

    # Determine overall class performance
    class_level = determine_class_performance(
        averages["average_final"]
    )

    # Display final summary
    display_performance_summary(
        df,
        averages,
        class_level,
        pass_percentage
    )

    # Display completion message
    display_completion_summary()


if __name__ == "__main__":
    main()