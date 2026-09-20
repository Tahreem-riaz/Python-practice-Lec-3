"""
========================================================
           LECTURE 03 - FILE 3: LIST METHODS
========================================================
Topics: List Methods
Total Questions: 10
========================================================
"""

# ==========================================
# PART A: ADDING ELEMENTS
# ==========================================

# Q1. Create a list containing three programming
#     languages.
#
#     Use append() to add two more languages.
#     Print the updated list.

languages = ["Python", "C++", "Java"]

languages.append("JavaScript")
languages.append("C#")

print("Updated list:", languages)

# ------------------------------------------

# Q2. Create a list of three numbers.
#
#     Use insert() to place a new number at the
#     beginning of the list.
#
#     Print the result.

numbers = [20, 30, 40]

numbers.insert(0, 10)
print("Updated list:", numbers)

# ------------------------------------------

# Q3. Create two lists containing different items.
#
#     Use extend() to combine the second list
#     with the first one.

list1 = ["Apple", "Banana", "Mango"]
list2 = ["Orange", "Grapes", "Peach"]

list1.extend(list2)
print("Combined list:", list1)

# ==========================================
# PART B: REMOVING ELEMENTS
# ==========================================

# Q4. Create a shopping list containing at least
#     five items.
#
#     Use remove() to delete one item.
#     Use pop() to remove another item.
#
#     Print the list after each operation.

shopping_list = ["Milk", "Bread", "Eggs", "Apples", "Juice"]
shopping_list.remove("Bread")