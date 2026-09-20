"""
========================================================
          LECTURE 03 - FILE 5: MINI PROJECT
========================================================
Project: Student Course Tracker

Concepts Used:
- Lists
- List Indexing
- List Slicing
- List Methods
- Tuples
- Tuple Indexing
- Tuple Slicing
- Tuple Methods
- Lists vs Tuples
========================================================
"""

# --------------------------------------------------------
# STEP 1: STUDENT INFORMATION
# --------------------------------------------------------

# Student information is stored in a tuple because
# these details should remain fixed.

student_info = ("Ayesha", "BSAI-GIU-SP26-005", 1)

print("\nStudent Information:")
print("Name:", student_info[0])
print("Student ID:", student_info[1])
print("Semester:", student_info[2])

# --------------------------------------------------------
# STEP 2: COURSE LIST
# --------------------------------------------------------

# Courses are stored in a list because courses can
# be added or removed.

courses = [
    "Programming Fundamentals",
    "Calculus",
    "Discrete Structures",
    "Functional English",
    "ICT",
    "Database Systems"
]

print("\nCourse List:")
print(courses)

# --------------------------------------------------------
# STEP 3: DISPLAY COURSE INFORMATION
# --------------------------------------------------------

print("\nCourse Information:")
