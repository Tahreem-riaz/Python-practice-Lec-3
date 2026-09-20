"""
========================================================
             LECTURE 03 - FILE 4: TUPLES
========================================================
Topics: Tuples, Lists vs Tuples, Tuple Slicing,
        Tuple Methods
Total Questions: 10
========================================================
"""

# ==========================================
#  PART A: CREATING & ACCESSING TUPLES
# ==========================================

# Q1. A student record contains information that
#     should not normally be changed:
#
#     - Student ID
#     - Name
#     - Program
#     - Semester
#
#     Store this information in a tuple.
#
#     Print the complete record and the student's
#     name and program using indexing.

student = (105, "Ayesha", "BS Artificial Intelligence", 1)

print("Student Record:", student)
print("Name:", student[1])
print("Program:", student[2])

# ------------------------------------------
