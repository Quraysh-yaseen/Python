# Dictionaries are a useful type that allow us to store our data in key, value pairs.
# Dictionaries themselves are mutable, but, just like sets, dictionary keys can only be immutable types.
# We use dictionaries when we want to be able to quickly access data associated with a key.

nums = {1: "one", 2: "two", 3: "three"}
print(len(nums))

# Any type of object, mutable or immutable, can be used as a value but just like sets, dictionaries can only use immutable types as keys.
# That means you can use int, str, or even tuple as a key, but not a set, list, or other dictionary.

# accessing an item 
nums = {"one": 1, "two": 2, "three": 3}
print(nums["one"])

# To add a new key value pair to the dictionary, you’ll use square-bracket notation.
nums = {1: "one", 2: "two", 3: "three"}
nums[8] = "eight"
print (nums)
{1: 'one', 2: 'two', 3: 'three', 8: 'eight'}
#to check for a key in dict
8 in nums
# If you try to put a key into a dictionary that’s already there, you’ll just end up replacing it.
nums[8] = "oops, overwritten"
print(nums)
{1: 'one', 2: 'two', 3: 'three', 8: 'oops, overwritten'}
# Just like with lists an sets, you can add the contents of one dictionary to another with the update() method.
colors = {"r": "Red", "g": "Green"}
numbers = {1: "one", 2: "two"}
colors.update(numbers)
print (colors)
# some func 
my_dict = {10:"ten" , 11:"eleven"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())