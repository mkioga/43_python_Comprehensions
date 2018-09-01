
# ===================
# compchallenge1.py
# ===================

# Use the conditional expression from fizz buzz program to produce a list comprehension
# that returns the fizz buzz results

# if a number is divisible by 3, the value should be "fizz"
# if it is divisible by 5, the value should be "buzz"
# if it is divisible by both 3 and 5 (i.e. 15), the value should be "fizz buzz"
# Finally if none of those conditions apply, the value will be the number itself.

# Here is the "for loop" version of the code.

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
print("="*20)


# =================
# My solution:
# =================

results = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x) for x in range(1, 31)]
print(results)
print("="*20)

# Results:

# ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz',
# '16', '17', 'fizz', '19', 'buzz', 'fizz', '22', '23', 'fizz', 'buzz', '26', 'fizz', '28', '29', 'fizz buzz']

# =======================
# Trainers solution:
# =======================

# NOTE: we are converting the numbers to strings ( else str(x) ) because conprehension produces a tuple of strings
# And we would like the results to be of same type. fizz and buzz and the number converted to string.

fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x) for x in range(1, 31)]
print(fizzbuzz)
print("="*20)

# Results:

# ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz',
# '16', '17', 'fizz', '19', 'buzz', 'fizz', '22', '23', 'fizz', 'buzz', '26', 'fizz', '28', '29', 'fizz buzz']


# We can also display it in different format.
# NOTE that this display is possible because all values are of same type i.e. strings
# NOTE: if you changed str(x) to x (to remain int), in above expression, the display below would give an error because
# int does not have a center function: Error message: AttributeError: 'int' object has no attribute 'center'

# So it is advisable to keep your list of same type so you can do things with it uniformly


for buzz in fizzbuzz:
    print(buzz.center(9, '*'))  # Values Centered, total width is 9 digits, and unused space filled with *

# Results:

# ****1****
# ****2****
# ***fizz**
# ****4****
# ***buzz**
# ***fizz**
# ****7****
# ****8****
# ***fizz**
# ***buzz**
# ****11***
# ***fizz**
# ****13***
# ****14***
# fizz buzz
# ****16***
# ****17***
# ***fizz**
# ****19***
# ***buzz**
# ***fizz**
# ****22***
# ****23***
# ***fizz**
# ***buzz**
# ****26***
# ***fizz**
# ****28***
# ****29***
# fizz buzz
