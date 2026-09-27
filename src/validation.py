"""Project configuration settings for student performance analysis."""

# Project information
PROJECT_NAME = "Student Performance Analysis"

# Performance thresholds
EXCELLENT_MARKS = 85
GOOD_MARKS = 70
MINIMUM_PASSING_MARKS = 40

# Data validation limits
MIN_MARKS = 0
MAX_MARKS = 100

MIN_ATTENDANCE = 0
MAX_ATTENDANCE = 100

MIN_STUDY_HOURS = 0

# Supported performance categories
SUPPORTED_CATEGORIES = [
    "Excellent",
    "Good",
    "Needs Improvement"
]