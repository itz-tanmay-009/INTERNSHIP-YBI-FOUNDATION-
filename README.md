
# Student Performance Analysis Using Python

A Python-based data analysis project that studies student academic performance using marks, study hours, attendance, and assignment scores.

The project uses data analysis and visualization techniques to summarize academic results, identify students who may need support, and understand patterns in student performance.

## Project Objectives

- Analyze student academic performance.
- Calculate average marks, attendance, study hours, and assignment scores.
- Identify the highest- and lowest-performing students.
- Classify students into performance categories.
- Analyze correlations between academic factors and final marks.
- Validate the dataset before analysis.
- Generate visualizations and summary reports.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook / Google Colab
- Git and GitHub

## Project Features

### 1. Dataset Management
Works with student records containing study hours, attendance, assignment scores, previous marks, and final marks.

### 2. Data Validation
Checks the dataset for common data quality issues, including missing values, duplicate student IDs, invalid marks, and incorrect numeric values.

### 3. Statistical Analysis
Calculates average values, median, standard deviation, minimum marks, and maximum marks.

### 4. Performance Classification
Groups students into performance categories based on their final marks.

### 5. Correlation Analysis
Examines relationships between study hours, attendance, assignment scores, previous marks, and final marks.

### 6. Student Improvement Analysis
Calculates the average change between previous marks and final marks to help understand academic progress.

### 7. Data Visualization
Uses Matplotlib to create charts that help present academic performance and related patterns.

### 8. Grade Summary and Reports
Generates grade summaries and a text report containing key performance statistics.

## Dataset Information

The project uses a sample dataset of 20 student records.

The dataset includes:

| Column | Description |
|---|---|
| Student_ID | Unique student identifier |
| Study_Hours | Hours spent studying |
| Attendance | Attendance percentage |
| Assignment_Score | Assignment marks |
| Previous_Marks | Marks from a previous assessment |
| Final_Marks | Final examination marks |

**Note:** The dataset is synthetic and intended for educational analysis. Its results should not be treated as conclusions about real students.

## Project Structure

```text
Student_Performance_Analysis/
├── notebook/
│   └── Student_Performance_Analysis.ipynb
├── src/
│   ├── main.py
│   ├── data.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── validation.py
│   ├── report.py
│   └── grade_summary.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/itz-tanmay-009/YBI-Foundation-Internship.git
```

### 2. Open the project folder

```bash
cd YBI-Foundation-Internship
```

### 3. Create a virtual environment (optional)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the analysis

```bash
python .\src\main.py
```

If the project uses local module imports, run the command from the `src` directory instead if necessary:

```powershell
cd .\src
python main.py
```

## Google Colab Notebook

The original project notebook is available here:

[Open Student Performance Analysis in Google Colab](https://colab.research.google.com/drive/1G4ios8vYG3oFUhDXttACsuwVUzAyZmPF?usp=sharing)

## Learning Outcomes

Through this project, I practiced:

- Python programming and modular code organization.
- Data manipulation with Pandas and NumPy.
- Statistical analysis of datasets.
- Data validation and error checking.
- Data visualization with Matplotlib.
- Generating reports and summaries.
- Using Git and GitHub for version control.

## Project Context

This project was developed as part of my Python programming and data analysis learning journey.

## Author

**Tanmay Kumar Mallick**

GitHub: [itz-tanmay-009](https://github.com/itz-tanmay-009)

---

*Built for learning Python, data analysis, and data visualization.*
