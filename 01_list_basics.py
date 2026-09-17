"""
========================================================
              LECTURE 03 - FILE 1: LISTS
========================================================
Topics: Lists, List Elements, Strings vs Lists
Total Questions: 8
========================================================
"""


# ==========================================
# PART A: CREATING LISTS
# ==========================================

# Q1. Create a list containing the names of five
#     programming languages.
#
#     Print the complete list.
#     Then print the first and last element.

languages = ["Python", "C++", "Java", "JavaScript", "C#"]
print(languages)
print("First element:", languages[0])
print("Last element:", languages[-1])

# ------------------------------------------

# Q2. Create a list containing different types of
#     information about a laptop:
#
#     - Brand
#     - RAM
#     - Price
#     - Is it available?
#
#     Print the list and each individual element.

laptop = ["HP", "8 GB", 85000, True]
print(laptop)
print("Brand:", laptop[0])
print("RAM:", laptop[1])
print("Price:", laptop[2])
print("Is it available?", laptop[3])


# ==========================================
# PART B: LIST INDEXING
# ==========================================

# Q3. Create a list of six numbers.
#
#     Use indexing to print:
#     - Second element
#     - Fourth element
#     - Last element
#     - Second-last element
#
#     Use both positive and negative indexes.

numbers = [10, 20, 30, 40, 50, 60]
