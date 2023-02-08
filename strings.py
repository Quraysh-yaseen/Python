"""Strings in Python can be enclosed either with single quotes like 'hello' or double quotes, like "hello".
To use the same type of quote within a string, that quote needs to be escaped with a \ - backwards slash."""

a_string = 'Hello, it\'s quraysh.'

# Strings can be printed out using the print() function 
print(a_string)

#Concatenation
#Strings can also be concatenated (added together) using the + operator to combine an arbitrary number of Strings.
b_string = " how are you?"
print (a_string + b_string)

# f-strings
# f-strings start with the letter f. Variables and expressions can be inserted into the string by enclosing them in curly brackets.
print (f"hello{b_string}")