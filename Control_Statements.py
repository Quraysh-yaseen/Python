# if in Python means: only run the rest of this code once, if the condition evaluates to True.
if 3 < 5:
    print("Hello, World!")

# If you only want your code to run if the expression is False, use the not keyword.
b = False
if not b:
    print("Negation in action!")

# if statements also work with items that have a “truthiness” to them.

message = "Hi there."
a = 0
if a:   # 0 is False-y
    print(message)
b = -1
if b:  # -1 is Truth-y
    print(message)
c = []
if c:  # Empty list is False-y
    print(message)
d = [1, 2, 3]
if d:  # List with items is Truth-y
    print(message)
e = ""
if e:
    print(message)


# if Statements and functions
def modify_name(name):
   if len(name) < 5:
        return name.upper()
   else:
        return name.lower()
name = "Nina"
print (modify_name(name))


# Nested if Statements
def num_info(num):
   if num > 0:
       print("Greater than zero")
       if num > 10:
           print("Also greater than 10.")
num_info(15)

# If we want to explicitly check if the value is explicitly set to True or False, we can use the is keyword.

a = True        # a is set to True
b = [1, 2, 3]   # b is a list with items, is "truthy"
if a is True:   # we can explicitly check if a is True
    print("hi")
if b:  # b is a list with items, is "truthy"
    print("Hello")
if b is True:   # b does not contain the actual value of True.
    print("Hola")


# The else statement is what you want to run if and only if your if statement wasn’t triggered.

a = True
if a:
    print("Hello")
else:
    print("Goodbye")

# elif means else if. It means, if this if statement isn’t considered True, try this instead.

a = 5
if a > 10:
    print("Greater than 10")
elif a < 10:
    print("Less than 10")
elif a < 20:
    print("Less than 20")
else:
    print("Dunno")





