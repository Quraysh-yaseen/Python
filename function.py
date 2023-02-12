# A function in Python is defined with the def keyword, followed by the function names, zero or more arguments or named arguments contained in parenthesis (), and a colon : to indicate the start of the function.
# A Basic Function that accepts no arguments and returns nothing.
def hello_world():
    print("Hello, World!")


# A Function that accepts two arguments, and returns a value
def add_numbers(x, y):
    print(x + y)


hello_world()
add_numbers(2,3)

# arguements
# Positional arguments are all required, and must be given in the order they are declared.
def say_greeting(name, greeting):
    print(f"{greeting}, {name}.")

    
say_greeting("quraysh", "Hello!")
 
 #Remember to never use an empty list as a default value to a function.