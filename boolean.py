# Truthiness
# Evaluating expressions to be True or False will help us control the flow of our program.
# If you want to test your assumptions about an expression that returns True or False, you can pass it into the constructor for booleans: bool(expression).


# In Python, the integer 0 is always False, while every other number, including negative numbers, are True. In fact, under the hood, booleans inherit from integers.
print(bool(0))
print(bool(1))
print(bool(-1))

#Empty sequences in Python always evaluate to False, including empty strings.
print(bool(""))    # String
print(bool(([])))    # Empty List
print(bool(set())) # Empty Set
print(bool({}))    # Empty Dictionary
print(bool(()))    # Empty Tuple

#Sequences with at least one value will evaluate to True.
print(bool("Hello"))   # String
print(bool([1]))       # List
print(bool({1}))       # Set
print(bool({1: 1}))    # Dictionary
print (bool((1,)))      # Tuple

# The None type in Python represents nothing. No returned value. It shouldn’t come as a surprise that the truthiness of None is False.
print(bool(None))




# Comparisons
print(1 < 10)  # 1 is less than 10? True
print(20 <= 20)  # 20 is less than or equal to 20? True
print(10 > 1)  # 10 is greater than 1? True
print(-1 > 1)  # -1 is greater than 1? False
print(30 >= 30)  # 30 is greater than or equal to 30? True

# Equality
#The equality operators val1 == val2 (val1 equals val2) and val1 != val2 (val1 doesn’t equal val2) compare the contents of two different values and return a boolean.

a = 1
b = 1
print(a == b)
print(a != b)
a = "Nina"
b = "Nina"
print(a == b)
print(a != b)
