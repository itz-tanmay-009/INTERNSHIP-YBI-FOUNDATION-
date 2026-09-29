## Data Validation

The project checks the dataset before performing analysis.

- Confirms that all required columns are present.
- Checks that the dataset is not empty.
- Prevents duplicate student IDs.
- Ensures marks are between 0 and 100.
- Checks that attendance is between 0 and 100.
- Ensures study hours are not negative.

These checks help identify invalid data before analysis begins.
# Student Performance Analysis Using Python

A Python-based data analysis project that examines student academic performance using study hours, attendance, assignment scores, previous marks, and final examination marks.

---

## Project Overview

**Student Performance Analysis Using Python** is a data analysis project developed as part of a Python Programming for AI & Data Science internship.

The project uses Python and popular data analysis and visualization libraries to process a student dataset, calculate statistical measures, identify performance patterns, analyze correlations, classify students based on their final marks, and visualize the results.

The project demonstrates practical applications of Python in:

- Data handling
- Data analysis
- Statistical calculations
- Correlation analysis
- Data visualization
- Performance classification
- CSV data export

---

## Project Objectives

The main objectives of this project are:

1. Analyze student academic performance using Python.
2. Examine the relationship between study hours and final marks.
3. Analyze the relationship between attendance and academic performance.
4. Study the relationship between assignment scores and final marks.
5. Compare previous marks with final examination performance.
6. Calculate important statistical measures.
7. Identify the highest and lowest performing students.
8. Classify students into performance categories.
9. Generate visual representations of the analysis.
10. Export the analyzed dataset to a CSV file.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Google Colab | Notebook-based development |
| Git | Version control |
| GitHub | Source code hosting |

---

## Dataset

The project uses a manually created synthetic dataset containing information about **20 students**.

The dataset includes the following attributes:

| Column | Description |
|---|---|
| `Student_ID` | Unique identifier for each student |
| `Study_Hours` | Number of hours spent studying |
| `Attendance` | Student attendance percentage |
| `Assignment_Score` | Assignment performance score |
| `Previous_Marks` | Marks obtained in previous examinations |
| `Final_Marks` | Final examination marks |

### Dataset Characteristics

- Total students: **20**
- Total attributes: **6**
- Final marks range: **47–97**
- Study hours range: **1–9 hours**
- Attendance range: **60–98%**

> **Note:** The dataset is synthetic and manually created for educational and demonstration purposes. It does not represent real student records.

---

## Project Structure

```text
Student_Performance_Analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebook/
│   └── Student_Performance_Analysis.ipynb
│
└── src/
    ├── main.py
    ├── data.py
    ├── analysis.py
    ├── visualization.py
    └── validation.py