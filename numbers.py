#There are three different types of numbers in Python: int (integer), float, and complex.

# These are all integers
x = 4
y = -193394
z = 0

# These are all floats
x = 5.0
y = -3983.2
z = 0.

# This is a complex number
x = 42j
type(x)

# to switch your variable between different types use
x = int(4)
z = float(5.0)
# To create a new integer from a string input, call int():
y = int('4')
y
type(y)

#Mathematical Operations
5 + 4
10 - 7
a = 3
b = 2
a * b  # multiplication
a ** b  # pow -- 3^2
5.0 / 2.0
# Use parenthesis to guarantee order
(2 + 2) * (3 + 5)
# Note: If you add a float and an int, the resulting type will be a float.
# If you divide two ints (integers), the result will be of type float, unless you use the special integer division operator (//) 
3.0 + 1
6 / 3
6 // 3

#Python also has several handy built-in methods for working with numbers, like min() for minimum, max() for maximum, and round() for rounding to the nearest integer.
min(3, 1, 2)
1
max(100, 0, 5)
100
round(3.1)
3
round(5.9)
6

