"""Python provides a built-in function for opening files, cleverly titled open().
The open() method will return an object that you can read() to get the data.
By default, open() will open a file in read-only mode, however you can change this by passing a mode parameter."""

my_file = open("my_file.txt")
my_file = open("my_file.txt", "w")
my_file = open("my_file.txt", "a")


""""A Context Manager is like a wrapper around a block of code that depends on some resource.
 It’s a safer way of handling resources than, say, using open() and then remembering to close() later (and hoping your program doesn’t crash in between). 
 It’s similar to using try... finally, but cleaner to look at.
 Context managers can contain code that auto-magically provisions a resource before your code runs, and cleans up afterward"""

with open("my_file.text") as my_file:
    contents = my_file.read()
