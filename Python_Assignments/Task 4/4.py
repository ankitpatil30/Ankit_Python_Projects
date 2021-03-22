# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

items=[n for n in input("Enter the hyphen-seperated string sequence: ").split('-')]
items.sort()
print("Sorted Sequence: ", '-'.join(items))
