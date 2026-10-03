# Student Performance Analysis Using Python

## Project Overview

Student Performance Analysis is a Python-based data analysis project that studies students' academic performance using marks, attendance, study hours, and assignment scores.

The project uses Pandas, NumPy, and Matplotlib to organize, analyze, and visualize student data. It also generates reports and grade summaries to make the results easier to understand.

## Project Objectives

- Analyze students' academic performance.
- Calculate average marks and attendance.
- Identify the highest- and lowest-performing students.
- Group students based on their final marks.
- Study the relationship between study hours, attendance, and marks.
- Generate charts and summary reports.
- Export analysis results into CSV files.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab
- Git and GitHub

## Project Features

### 1. Data Management
Stores student information, including student ID, study hours, attendance, assignment marks, and final marks.

### 2. Data Analysis
Calculates:
- Average final marks
- Average study hours
- Average attendance
- Highest and lowest marks
- Student performance categories
- Pass and fail statistics
- Correlation between numerical columns

### 3. Data Validation
Checks the dataset for:
- Missing required columns
- Empty data
- Duplicate student IDs
- Invalid marks
- Invalid attendance values
- Negative study hours

### 4. Data Visualization
Creates charts to present student performance, including:
- Performance category chart
- Final marks distribution
- Study hours versus final marks
- Attendance versus final marks
- Grade distribution

### 5. Grade Classification

Students are assigned grades according to their final marks:

| Grade | Marks Range |
|---|---|
| A | 90–100 |
| B | 80–89 |
| C | 70–79 |
| D | 40–69 |
| F | Below 40 |

The project calculates the number and percentage of students in each grade.

### 6. Report Generation
Generates a summary report containing important performance statistics, including pass and fail information.

### 7. CSV Export
The project can save grade summaries and individual student grades as CSV files.

## Project Structure

```text
Student_Performance_Analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── data.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── validation.py
│   ├── report.py
│   └── grade_summary.py
│
└── notebook/
    └── Student_Performance_Analysis.ipynb