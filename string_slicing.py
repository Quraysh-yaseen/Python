# Slicing is a easy way to create sub-lists from larger lists.
my_string = "Hello, world!"
print(my_string[7:12]) # from 7 to 12

# Lopsided Slicing
print(my_string[:5]) # from zero to 5
print(my_string[7:]) # from 7 to the end

# Negative Indexing
print(my_string[-6:]) # from the end - 6 to the end
print(my_string[-10:-4]) # from the end - 10 to the end - 4

# Python slices also have a third, optional argument, called “step” or “stride”, separated by a second colon. 
# This lets you skip elements of a list or even reverse them.

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[::2]) # move forward by 2, or skip every other index
print(my_list[::-1]) # move backward by 1, and easy way to reverse a list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(my_list[1:7:2]) # get every other index between 1 and 7

