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

print("After remove():", shopping_list)
shopping_list.pop(1)

print("After pop():", shopping_list)

# ------------------------------------------

# Q5. Create a list of numbers.
#
#     Use pop() without specifying an index.
#
#     Print:
#     - The removed value
#     - The updated list

numbers = [10, 20, 30, 40, 50]

removed_value = numbers.pop()
print("Removed value:", removed_value)
print("Updated list:", numbers)

# ==========================================
# PART C: SORTING & REVERSING
# ==========================================

# Q6. Create a list of numbers in random order.
#
#     Sort the list in ascending order and print it.
#     Then reverse the sorted list.

numbers = [50, 20, 80, 10, 40, 30]
numbers.sort()

print("Ascending order:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

# ------------------------------------------

# Q7. Create a list containing several names.
#
#     Sort the names alphabetically.
#     Print the sorted list.

names = ["Zain", "Ali", "Sara", "Ahmed", "Hina"]

names.sort()
print("Alphabetically sorted:", names)

# ==========================================
# PART D: SEARCHING & COUNTING
# ==========================================

# Q8. Create a list containing repeated numbers.
#
#     Use count() to find how many times a particular
#     number appears.

numbers = [10, 20, 10, 30, 10, 40, 20]

count = numbers.count(10)
print("Number of times 10 appears:", count)

# ------------------------------------------

# Q9. Create a list of programming languages.
#
#     Use index() to find the position of a language
#     in the list.

languages = ["Python", "C++", "Java", "JavaScript", "C#"]

position = languages.index("Java")

print("Position of Java:", position)

# ==========================================
# PART E: CHALLENGE
# ==========================================

# Q10. Create a list of five products.
#
#      Perform the following operations:
#
#      - Add a new product
#      - Insert a product at a specific position
#      - Remove a product
#      - Sort the list
#      - Reverse the list
#
#      Print the list after each operation.

products = ["Laptop", "Mouse", "Keyboard", "Headphones", "Monitor"]

# Add a new product
products.append("Webcam")
print("After adding:", products)
