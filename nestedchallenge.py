
# ======================
# nestedchallenge.py
# ======================

# In an earlier lesson, we used a "for loop" to print the times table, for values from 1 to 10.
# We used a nested loop shown below.

for i in range(1, 5):
    for j in range(1, 5):
        print("i = {}: j = {}: i x j = {}".format(i, j, i * j))
print("="*20)

# Results:

# i = 1: j = 1: i x j = 1
# i = 1: j = 2: i x j = 2
# i = 1: j = 3: i x j = 3
# i = 1: j = 4: i x j = 4
# i = 2: j = 1: i x j = 2
# i = 2: j = 2: i x j = 4
# i = 2: j = 3: i x j = 6
# i = 2: j = 4: i x j = 8
# i = 3: j = 1: i x j = 3
# i = 3: j = 2: i x j = 6
# i = 3: j = 3: i x j = 9
# i = 3: j = 4: i x j = 12
# i = 4: j = 1: i x j = 4
# i = 4: j = 2: i x j = 8
# i = 4: j = 3: i x j = 12
# i = 4: j = 4: i x j = 16


# ============
# Challenge:
# ============

# Challenge is to use a nested comprehension to produce the same values.
# You can iterate over the list, to produce the same output as the "for loop".
# Or just print out the list


# =============
# My solution:
# =============

print("My solution:")
for multiples in [("i = {}: j = {}: i x j = {}".format(i, j, i * j)) for i in range(1, 5) for j in range(1, 5)]:
    print(multiples)
print("="*20)

# Results:

# My solution:
# i = 1: j = 1: i x j = 1
# i = 1: j = 2: i x j = 2
# i = 1: j = 3: i x j = 3
# i = 1: j = 4: i x j = 4
# i = 2: j = 1: i x j = 2
# i = 2: j = 2: i x j = 4
# i = 2: j = 3: i x j = 6
# i = 2: j = 4: i x j = 8
# i = 3: j = 1: i x j = 3
# i = 3: j = 2: i x j = 6
# i = 3: j = 3: i x j = 9
# i = 3: j = 4: i x j = 12
# i = 4: j = 1: i x j = 4
# i = 4: j = 2: i x j = 8
# i = 4: j = 3: i x j = 12
# i = 4: j = 4: i x j = 16


# ====================
# Trainers solution 1:
# ====================
# It is same as mine but you can unpack the output in LINE_1

print("Trainers solution 1:")
for i, j, ij in [(i, j, i * j) for i in range(1, 5) for j in range(1, 5)]:  # LINE_1
    print("i = {}: j = {}: i x j = {}".format(i, j, ij))
print("="*20)

# Results:

# Trainers solution 1:
# i = 1: j = 1: i x j = 1
# i = 1: j = 2: i x j = 2
# i = 1: j = 3: i x j = 3
# i = 1: j = 4: i x j = 4
# i = 2: j = 1: i x j = 2
# i = 2: j = 2: i x j = 4
# i = 2: j = 3: i x j = 6
# i = 2: j = 4: i x j = 8
# i = 3: j = 1: i x j = 3
# i = 3: j = 2: i x j = 6
# i = 3: j = 3: i x j = 9
# i = 3: j = 4: i x j = 12
# i = 4: j = 1: i x j = 4
# i = 4: j = 2: i x j = 8
# i = 4: j = 3: i x j = 12
# i = 4: j = 4: i x j = 16

# ================================================
# Trainers solution 2: - Using list comprehension
# ================================================
# Using a list comprehension
# NOTE that this unpacks all the info in one list and can take a lot of memory if range is big

print("Trainers solution 2:")
times = [(i, j, i * j) for i in range(1, 5) for j in range(1, 5)]
print(times)
print("="*20)

# Results:

# Trainers solution 2:
# [(1, 1, 1), (1, 2, 2), (1, 3, 3), (1, 4, 4), (2, 1, 2), (2, 2, 4), (2, 3, 6), (2, 4, 8), (3, 1, 3), (3, 2, 6), (3, 3, 9), (3, 4, 12), (4, 1, 4), (4, 2, 8), (4, 3, 12), (4, 4, 16)]



# ====================================================
# Trainers solution 3: - Using Generator Expression:
# ====================================================

# if you just want to iterate over the list, then a "generator expression" is more suitable than a "list comprehension".
# NOTE that in generator expression, we enclose in ( ) instead of [ ] on LINE_1 below
# Generators do not create entire list in memory.
# Generator expressions calculate values as they are requested. The only value that exist is the one that is being returned.


print("Trainers solution 3: Generator Expression:")
for i, j, ij in ((i, j, i * j) for i in range(1, 5) for j in range(1, 5)):  # LINE_1
    print("i = {}: j = {}: i x j = {}".format(i, j, ij))
print("="*20)

# Results:

# Trainers solution 3: Generator Expression:
# i = 1: j = 1: i x j = 1
# i = 1: j = 2: i x j = 2
# i = 1: j = 3: i x j = 3
# i = 1: j = 4: i x j = 4
# i = 2: j = 1: i x j = 2
# i = 2: j = 2: i x j = 4
# i = 2: j = 3: i x j = 6
# i = 2: j = 4: i x j = 8
# i = 3: j = 1: i x j = 3
# i = 3: j = 2: i x j = 6
# i = 3: j = 3: i x j = 9
# i = 3: j = 4: i x j = 12
# i = 4: j = 1: i x j = 4
# i = 4: j = 2: i x j = 8
# i = 4: j = 3: i x j = 12
# i = 4: j = 4: i x j = 16



# =======================================================
# Performance, speed and memory usage differences
# when using list expressions and generator expressions
# =======================================================

# Python has a "timeit" module that you can use to compare the performance of different code snippets.
# We will work on that in the next section

