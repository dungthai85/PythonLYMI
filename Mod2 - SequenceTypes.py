
# Reading Comprehensions

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