#Set comprehensions are another great operation in Python - they look like a cross between list and dict comprehensions, and they create set objects.
#Notice that instead of returning the same list of numbers (as num for num would have done in a list comprehension), you instead get a set (note the curly braces) of unique numbers from the list (you only get one 1).
my_set = {num for num in [1, 2, 1, 0, 3]}
print(my_set) 


"""Generator expressions are a more advanced concept.
A generator is a type of iterable object - like a list, you can iterate through each element - however, unlike a list, generators evaluate elements on demand, instead of assembling them all at once."""

list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
print(list_comp)
# we get [0, 4, 16, 36, 64]

gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(gen_exp)
# we get <generator object <genexpr> at 0x000001A1F1B45E00>
for num in gen_exp:
    print(num)