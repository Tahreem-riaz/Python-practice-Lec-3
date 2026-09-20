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

# ==========================================
# PART B: STEP SLICING
# ==========================================

# Q3. Create a list of numbers from 1 to 15.
#
#     Use slicing with a step to print:
#     - Every second number
#     - Every third number

numbers = list(range(1, 16))

print("Every second number:", numbers[::2])
print("Every third number:", numbers[::3])

# ------------------------------------------

# Q4. Create a list containing the days of the week.
#
#     Use slicing with a step to select alternate days.

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

print("Alternate days:", days[::2])

# ==========================================
# PART C: NEGATIVE SLICING
# ==========================================

# Q5. Create a list containing eight different
#     fruits.
#
#     Use negative slicing to extract the last
#     four fruits.

fruits = ["Apple", "Banana", "Mango", "Orange",
          "Grapes", "Peach", "Watermelon", "Strawberry"]

print("Last four fruits:", fruits[-4:])

# ------------------------------------------

# Q6. Create a list of numbers.
#
#     Use negative slicing to remove the first
#     few elements and display the remaining list.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Remaining list:", numbers[-5:])

# ==========================================
# PART D: REVERSE SLICING
# ==========================================

# Q7. Create a list containing the numbers 1 to 10.
#
#     Use slicing with a negative step to reverse
#     the list.

subjects = ["English", "Mathematics", "Programming", "Physics", "ICT"]

subjects[2] = "Artificial Intelligence"
subjects.append("Database")

print("Updated subjects:", subjects)
# ------------------------------------------

# Q8. Create a "Shopping Cart" list containing
#     at least five items.
#
#     Print:
#     - Complete cart
#     - First item
#     - Last item
#     - Total number of items

shopping_cart = ["Milk", "Bread", "Eggs", "Apples", "Juice"]

