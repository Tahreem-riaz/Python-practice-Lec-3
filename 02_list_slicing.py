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
