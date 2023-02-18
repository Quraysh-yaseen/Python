# for loop
colors = ["Red", "Green", "Blue", "Orange"]
for color in colors:
    print(f"The color is: {color}")

# Looping over items with the index using enumerate.
print (enumerate (colors))
list (enumerate (colors)) #list generator
for index , color in enumerate(colors):
    print(f"{index},{color}")

# Looping over a dictionary
hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF",
}

for color, hex_value in hex_colors.items():
    print(f"For color {color}, the hex value is: {hex_value}")

# while loops 
# while loops are a special type of loop in Python. 
# Instead of running just once when a condition is met, like an if statement, they run forever until a condition is no longer met.
 
counter = 0
max_val = 4
while counter < max_val:
    print(f"The count is: {counter}")
    counter = counter + 1
# Just like in functions, consider the return statement the hard kill-switch of the loop.

def name_length(names):
    for name in names:
            print(name)
            if name == "Nina":
                return print("Found the special name")
names = ["Max", "Nina", "Rose"]
name_length(names)