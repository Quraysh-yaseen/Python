"""a list is a collection of ordered, mutable, and changeable elements that can store elements of different data types, including numbers, strings, and objects.
Lists are written with square brackets [] and elements are separated by commas."""

fruits = ['apple', 'banana', 'cherry']
#some common methods 
fruits.append('orange')
fruits.insert(1, 'mango')
fruits.remove('banana')
print(fruits) # Output: ['apple', 'mango', 'cherry', 'orange']
fruits.sort()
print(fruits) # Output: ['apple', 'cherry', 'mango', 'orange']
fruits.reverse()
print(fruits) # Output: ['orange', 'mango', 'cherry', 'apple']