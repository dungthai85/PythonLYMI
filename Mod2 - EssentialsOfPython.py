#Reading Comprehension

#Boolean Expresions

# Assuming x is a an integer-type, write a comparison statement that will 
# return True if x is an even number, and False otherwise. (Hint: recall the purpose of the % operator)

import math as m

def iseven(x):
    if x % 2 == 0:
        return True
    else:
        return False

print("Is Even?", iseven(6))
print("Is Even?", iseven(7))

# Assuming x and y are both real-valued numbers (i.e. not complex numbers), 
# write a line of code that will return False if: x and y are within 0.9 of one another, 
# and x is a positive number. (Hint: try writing the expression that will return True for this condition, and then negate it)

def isclosepositive(x, y):
    close = (abs(x-y)) < 0.9
    return not close and x > 0


print("Is CLose and x is Positive?", isclosepositive(1.5, 0.7))
print("Is CLose and x is Positive?", isclosepositive(1.5, 3.7))

# Write an expression that returns True if x is a boolean-type object or a float-type object.

def typeChecker(x):
    return isinstance(x, bool) or isinstance(x, float)


print("Is Boolean or Float?", typeChecker(True))
print("Is Boolean or Float?", typeChecker(2))
print("Is Boolean or Float?", typeChecker(2.3))

# Strings

# Use a function that will take the string "cat", and returns the string "   cat    " 
# (which has a length of 11, including the letters c, a, t). Now, change the way you call the 
# function so that it returns "----cat----" instead.

def addSpace(x):
    # x.center(11)
    # x.center(11, "-")
    return ('{:^11}'.format(x)).replace(" ", "-")

print(addSpace("cat"))

# Replace the first three periods of this string with a space-character: "I.am.aware.that.spaces.are.a.thing"

def replaceperiod(x):
    return x.replace(".", " ", 3)

print(replaceperiod("I.am.aware.that.spaces.are.a.thing"))

# Remove the whitespace from both ends of: "  basket    "

def removewhite(x):
    return x.strip()

print(removewhite("  basket    "))

#Create a string that will print as (the second line begins with a tab-character):

print('Hello\n\tover there')

# Convert the integer 12 to the string "12".

num = str(12)
print("Is this a string:", isinstance(num, str))

# Only kids 13 and up are allowed to see Wayne’s World. Given the variables name (a string) 
# and age (an integer), use an f-string that will display: “NAME is old enough to watch the movie: BOOL”, 
# where NAME is to be replaced with the kid’s name, and BOOL should be True if the kid is at least 13 years old, and False otherwise.

def fstring(name, age):
    return f"{name} is old enough to watch the movie: {age >= 13}"

print(fstring("John", 12))
print(fstring("Jane", 14))

# Lists

# Create a list whose sole entry is the None object.

mylist = [None]
print(mylist)

# Assign to the variable k a list that contains an integer, a boolean, and a string, in that order. 
# Then, add two more entries to the end of the list: a float and a complex number.

k = [10, True, "Hello"]
print(k)
k.extend([1.5, 5+3j])
print(k)

# Alphabetize the list of names: ["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"].

def sortList(x):
    x.sort()
    return x

print(sortList(["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"]))

#BasicObjectType Completed

######################################################################################################################

# Sequence Types

# Change the list [True, None, 22] into a tuple.

tuple([True, None, 22])

# How many sequence-types have we discussed thus far? 
# Which of these produce objects that are immutable? 
# Which of these produce objects that are mutable? 
# For those types that are mutable, write a piece of example code that mutates an object.

# 3 - strings, lists, and tuples
# Strings and Tuples
# Lists

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

# Given the tuple:
#   x = (0, 2, 4, 6, 8)

# Slice or index into x to produce the following:

x = (0, 2, 4, 6, 8)

# 1. 0

print(x[0])

# 2. 8 (using a negative index)

print(x[-1])

# 3. (2, 4, 6) (using a slice-object)

print(x[slice(1,-1,1)])

# 4. (4,)

print(x[2:3])

# 5. 4

print(x[2])

# 6. 4 (using a negative index)

print(x[-3])

# 7. (6, 8) (using a negative index for the start of the slice)

print(x[-2:])

# 8. (2, 6)

print(x[1:-1:2])

# 9. (8, 6, 4, 2)

print(x[slice(None, 0, -1)])

# Write a piece of code for each of the following tasks. If the task is impossible/ill-posed explain why.

# 1. Using the string “blogosphere”, slicing, and repeat-concatenation, create the string: ‘boopeeboopeeboopeeboopeeboopee’.
#    (hint: how would you slice “blogosphere” to produce “boopee”, think step-size)

boop = "blogosphere"

print(boop[::2]*5)

# 2. Assume that a tuple, x, contains the item 5 in it at least once. Find where that first entry is, 
#    and change it to -5. For example (1, 2, 5, 0, 5) → (1, 2, -5, 0, 5).

#   Tuples cannot be changed so thisis impossible

# 3. Given a sequence, x, and a valid negative index for x, neg_index, find the corresponding positive-value for that index. 
#    That is, if x = "cat", and neg_index = -3, which is the negative index that would return "c", then you would want to return the index 0.

x = "cat"
neg_index = -3
pos_index = neg_index + len(x)

print(pos_index)

# SequenceTypes Completed

###########################################################################################################

# Variables and Assignments

# Suppose x is assigned a list, and that y is assigned a “slice” of x. 
# Do x and y reference the same list? That is, if you update part of the 
# subsequence common to x and y, does that change show up in both of them? 
# Write some simple code to investigate this.

x = [1, 2, 3, 4]
y = x[slice(None, 2, 1)]

print(x)
print(y)
x[0] = 5
print(y)

# No. With my investigation, changing a common subsequence in x does not effect the original 
# slice of y

# Based on our discussion of mutable and immutable objects, 
# predict what the value of y will be in the following circumstance:

x = 3
y = x

x *= 3
print(x)
print(y)

# Variables & Assignments Completed

##########################################################################################################

# Control Flow

