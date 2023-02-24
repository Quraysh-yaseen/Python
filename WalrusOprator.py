"""The Walrus operator, also known as the assignment expression,
is a new feature introduced in Python 3.8. It allows you to assign
values to variables as part of an expression"""

# Count the number of vowels in a string

word = input("Enter a word: ")

vowel_count = 0

while (char := input().lower()) != "stop":
    if char in "aeiou":
        vowel_count += 1

print("The number of vowels in the word is:", vowel_count)

"""In this example, we are counting the number of vowels 
in a word entered by the user. We use the walrus operator 
to simplify the while loop by assigning the value of input().
lower() to the variable char and checking whether it is equal to "stop" 
in the same line. If char is not equal to "stop", we check if 
it is a vowel and increment the vowel_count variable if it is."""
