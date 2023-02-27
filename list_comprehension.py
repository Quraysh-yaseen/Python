# without using list comprehension 
names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
print(my_list)

# using list comprehension 
names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [len(name) for name in names]
print(my_list)

#conditionals
names = ["Nina", "Max", "Rose", "Jimmy"]
my_list1 = [name for name in names if len(name) % 2 == 0]
my_list2 = [name for name in names if len(name) % 2 != 0]
print(my_list1)
print(my_list2)

#Split and Join
name_string = "nina,max,jack"
name_list = name_string.split(",")

joined_names  = " - ".join(name_list)
print(joined_names)

# String Joining with a List Comprehension

my_list = [0, 1, 2, 3, 4]
my_string = ",".join([str(num) for num in my_list])
print(my_string)
