"""Dictionary comprehensions are a quick and easy way of assembling dictionaries in Python.
 They work just like list comprehensions, and look almost the same.
 They use curly braces instead of square brackets, and they contain two variables (for key and value), separated by a colon."""

squares = {num:num * num for num in range(10)}
print(squares)
scores = {f"player-{num}":0 for num in range(0, 5)}
print(scores)



my_list = [(f"player-{num}", num * 2) for num in range(0, 5)]
print(my_list)

scores_2 = {key:value for (key, value) in my_list}
print(scores_2)