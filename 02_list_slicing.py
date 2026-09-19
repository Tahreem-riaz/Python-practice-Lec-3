"""
========================================================
          LECTURE 03 - FILE 2: LIST SLICING
========================================================
Topics: List Slicing, Positive and Negative Slicing
Total Questions: 8
========================================================
"""

# ==========================================
# PART A: BASIC SLICING
# ==========================================

# Q1. Create a list containing the numbers from
#     10 to 100.
#
#     Use slicing to print:
#     - First five elements
#     - Last five elements
#     - Elements from the middle

numbers = list(range(10, 101))
print("First five elements:", numbers[:5])
print("Last five elements:", numbers[-5:])
print("Middle elements:", numbers[40:50])

# ------------------------------------------

# Q2. Create a list containing seven different
#     programming languages.
#
#     Use slicing to create:
#     - A list containing the first three
#     - A list containing the last three

languages = ["Python", "C++", "Java", "JavaScript", "C#", "PHP", "Ruby"]

first_three = languages[:3]
last_three = languages[-3:]

print("First three:", first_three)
print("Last three:", last_three)