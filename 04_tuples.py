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

student = (005, "Tahreem", "BS Artificial Intelligence", 2)

print("Student Record:", student)
print("Name:", student[1])
print("Program:", student[2])

# ------------------------------------------

# Q2. A GPS system stores the coordinates of a
#     location as a tuple:
#
#     coordinates = (31.5204, 74.3587)
#
#     Print the latitude and longitude separately.
#
#     Why is a tuple suitable here?
#     Write your answer as a comment.

coordinates = (31.5204, 74.3587)

print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# A tuple is suitable because the coordinates
# should remain fixed and should not be changed.


# ==========================================
# PART B: TUPLE INDEXING & SLICING
# ==========================================

# Q3. A student's weekly marks are stored in a tuple.
#
#     The order is:
#     Monday, Tuesday, Wednesday, Thursday, Friday
#
#     Print:
#     - Monday's marks
#     - Friday's marks
#     - Wednesday's marks
#
#     Use both positive and negative indexing.

weekly_marks = (78, 85, 91, 74, 88)

print("Monday:", weekly_marks[0])
print("Friday:", weekly_marks[-1])
print("Wednesday:", weekly_marks[2])

# ------------------------------------------

# Q4. A university timetable contains the subjects
#     for six periods.
#
#     Use slicing to display:
#     - Morning classes (first three)
#     - Afternoon classes (last three)
#     - Every alternate period

timetable = (
    "Programming",
    "Calculus",
    "English",
    "ICT",
    "Discrete Structures",
    "AI"
)

print("Morning classes:", timetable[:3])
print("Afternoon classes:", timetable[3:])
print("Alternate periods:", timetable[::2])

# ------------------------------------------

# Q5. A company stores the years in which an employee
#     received an award:
#
#     2019, 2020, 2021, 2022, 2023, 2024
#
#     Use negative slicing to display the three
#     most recent award years.

award_years = (2019, 2020, 2021, 2022, 2023, 2024)

recent_years = award_years[-3:]

print("Most recent award years:", recent_years)

# ==========================================
# PART C: LISTS VS TUPLES
# ==========================================

# Q6. A shopping cart changes frequently, while
#     a product's barcode should remain fixed.
#
#     Store:
#     - Shopping cart items in a list
#     - Product barcode in a tuple
#
#     Add a new item to the shopping cart.
#     Then explain why the barcode is stored in a tuple.

shopping_cart = ["Mouse", "Keyboard", "USB Cable"]

product_barcode = (8, 9, 2, 5, 1, 7)

shopping_cart.append("Headphones")

print("Updated shopping cart:", shopping_cart)
print("Product barcode:", product_barcode)

# The shopping cart is a list because its items
# can change.
# The barcode is a tuple because its values
# should remain fixed.

# ------------------------------------------

# Q7. A student's subjects may change during
#     registration, so they should be stored in
#     a list.
#
#     A student's date of birth does not normally
#     change, so store it in a tuple.
#
#     Print the type of both.

subjects = ["Programming", "Calculus", "English"]

date_of_birth = (14, "February", 2008)

print("Subjects type:", type(subjects))
print("Date of birth type:", type(date_of_birth))

# List = mutable and can be changed.
# Tuple = immutable and cannot be changed directly.

# ==========================================
# PART D: TUPLE METHODS
# ==========================================
