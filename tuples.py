"""A tuple in Python is a collection of ordered, immutable, and heterogeneous elements, separated by commas and enclosed within parentheses.
 Tuples are similar to lists in many ways, but there are some key differences between them."""

student = ("Marcy", 8, "History", 3.5)
# We can access items in the tuple by index.
student = ("Marcy", 8, "History", 3.5)
print(student[0])
# You can also use tuples for something called unpacking
student = ("Marcy", 8, "History", 3.5)
name, age, subject, grade = student
print(age)