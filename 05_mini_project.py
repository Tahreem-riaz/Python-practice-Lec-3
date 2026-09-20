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

# Complete course list
print("All courses:", courses)

# First course
print("First course:", courses[0])

# Last course
print("Last course:", courses[-1])

# First three courses
print("First three courses:", courses[:3])

# --------------------------------------------------------
# STEP 4: MODIFY THE COURSE LIST
# --------------------------------------------------------

# Add a new course
courses.append("Artificial Intelligence")

# Remove one course
courses.remove("ICT")

# Insert a course at position 2
courses.insert(2, "Object Oriented Programming")

print("\nUpdated Course List:")
print(courses)

# --------------------------------------------------------
# STEP 5: ORGANIZE THE COURSES
# --------------------------------------------------------

# Sort the course list alphabetically
courses.sort()

print("\nAlphabetically Sorted Courses:")
print(courses)

# Create a reversed version without changing
# the sorted list.
reversed_courses = courses[::-1]

print("\nReversed Courses:")
print(reversed_courses)

# --------------------------------------------------------
# STEP 6: COURSE ANALYSIS
# --------------------------------------------------------

# Number of courses
total_courses = len(courses)

print("\nCourse Analysis:")
print("Total number of courses:", total_courses)

# Position of a particular course
course_position = courses.index("Calculus")

print("Position of Calculus:", course_position)

# Check whether a course appears more than once
courses.append("Calculus")

calculus_count = courses.count("Calculus")

print("Calculus appears:", calculus_count, "times")

if calculus_count > 1:
    print("Calculus appears more than once.")
else:
    print("Calculus appears only once.")


# --------------------------------------------------------
# STEP 7: TUPLE PRACTICE
# --------------------------------------------------------

# These university details are fixed, so a tuple
# is suitable for storing them.

university_details = (
    "Green International University",
    "Lahore",
    "BSAI"
)

print("\nUniversity Details:")
print("Complete details:", university_details)

# Tuple indexing
print("University:", university_details[0])
print("Program:", university_details[2])

# Tuple slicing
print("University and Location:", university_details[:2])


# Tuple method
print("Position of BSAI:",
      university_details.index("BSAI"))

# --------------------------------------------------------
# EXTRA CHALLENGE
# --------------------------------------------------------
