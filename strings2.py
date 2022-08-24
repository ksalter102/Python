# number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using an separators: ")
seperators = "" #seperators = ',;:'

for char in number:
    if not char.isnumeric(): #will skip numbers / get rid of seperators e.g ;
        seperators = seperators + char
# char means charectors, usually digits
# print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))

# USE DEBUGGER TO SEE WHAT'S HAPPENING!

# SUM --------------
# sum(iterable, /, start=0)
# Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.
#
# For some use cases, there are good alternatives to sum().
# The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence).
# To add floating point values with extended precision, see math.fsum().
# To concatenate a series of iterables, consider using itertools.chain().