# Student Performance Analysis Using Python

A Python data analysis project that explores student academic performance using **Pandas, NumPy, and Matplotlib**. The project summarizes marks, attendance, study hours, and performance categories to help identify patterns in student results.

## Project Objectives

- Analyze student marks and academic performance.
- Calculate averages and pass percentages.
- Identify the highest- and lowest-scoring students.
- Compare previous marks with final marks.
- Examine attendance and study habits.
- Generate charts and summary reports.

## Technologies Used

- **Python** — core programming language
- **Pandas** — data handling and analysis
- **NumPy** — numerical operations and data validation
- **Matplotlib** — data visualization
- **CSV** — student dataset format
- **Jupyter Notebook / Google Colab** — interactive analysis

## Project Structure

```text
Student_Performance_Analysis/
├── data/
│   └── student_performance.csv
├── notebook/
│   └── Student_Performance_Analysis.ipynb
├── output/
├── src/
│   ├── main.py
│   ├── data.py
│   ├── validation.py
│   ├── analysis.py
│   ├── grade_summary.py
│   ├── visualization.py
│   └── report.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Some folders and generated files may appear only after running the project.*

## Features

- Load student records from a CSV file.
- Validate required columns and numeric values.
- Calculate average study hours, attendance, and marks.
- Find the top three students and the lowest-scoring student.
- Calculate the percentage of students who pass.
- Compare previous and final marks.
- Categorize students by final marks.
- Identify students who may need additional academic support.
- Generate visualizations and summary reports.

## Dataset

The dataset uses the following fields:

| Column | Description |
|---|---|
| `Student_ID` | Unique student identifier |
| `Study_Hours` | Study time in hours |
| `Attendance` | Attendance percentage |
| `Previous_Marks` | Marks obtained previously |
| `Assignment_Marks` | Assignment marks |
| `Final_Marks` | Final examination marks |

The project can use an existing CSV dataset or sample records provided by the Python data module. Sample records are illustrative and should not be interpreted as real student results.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/itz-tanmay-009/INTERNSHIP-YBI-FOUNDATION-.git
cd INTERNSHIP-YBI-FOUNDATION-
```

### 2. Create a virtual environment (optional)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

From the project root directory, run:

```bash
python src/main.py
```

The program is designed to perform the analysis and generate supported reports or charts in the output directory.

## Learning Outcomes

Through this project, I am developing practical skills in:

- Python programming and modular code organization
- Data cleaning and validation
- Data analysis with Pandas and NumPy
- Data visualization with Matplotlib
- Working with CSV files
- Generating analytical summaries and reports
- Managing project versions with Git and GitHub

## Project Scope

This is a **data analysis project, not a machine learning prediction system**. Its purpose is to summarize and understand student performance using descriptive statistics and visualizations.

## Internship

This project is part of my Python programming and data analysis learning journey with YBI Foundation.

## Author

**Tanmay Kumar Mallick**

GitHub: [itz-tanmay-009](https://github.com/itz-tanmay-009)

---

*This project is intended for educational purposes. Any sample dataset represents illustrative records, not verified academic records.*
