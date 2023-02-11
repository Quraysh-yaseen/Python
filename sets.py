"""A set is a mutable datatype that allows you to store immutable types in an unsorted way.
Sets are mutable because you can add and remove items from them.
They can contain immmutable items, like tuples and other primitive types, but not lists, sets, or dictionaries which are themselves mutable.
Unlike a list or a tuple, a set can only contain one instance of a unique item.
 There are no duplicates allowed.
The benefits of a set are: very fast membership testing along with being able to use powerful set operations, like union and intersection."""

# Creating a set using curly braces
fruits = {'apple', 'banana', 'cherry'}
print(fruits)

# Creating a set using the set() constructor
vegetables = set(['potato', 'carrot', 'onion'])
print(vegetables)

# Add items to a set with my_set.add(item)
colors = {"Red", "Green", "Blue"}
colors.add("Orange")
# Remove items with my_set.discard(item)

colors = {"Red", "Green", "Blue"}
colors.discard("Green")
# You can remove an item from a set if it’s present with my_set.discard(item). If the set doesn’t contain the item, no error occurs.
colors.discard("Green")
print(colors)
