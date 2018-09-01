
# ==============
# timeit1.py
# ==============

# ====================
# The timeit module
# ====================

# in section from nextedforloops.py, we saw three different ways to create the same output
# Now we want to determine which way performs better i.e how fast they run to produce results.

# We will use the code from nextedforloops.py below
# NOTE that we should make sure we are comparing like for like code.
# In this case, we are not and will comment out some code that we don't want to test.

# (1) The "nested for loop" creates 6 lists and discards each list before creating the next one. LINE_1

# (2) The "list comprehension inside a for loops"  does same thing. each time around the loop, the comprehension assigns
# a new list to "exits_to_destination_2": LINE_2

# (3) The "Nested comprehensions" builds up a nested list containing all six of the other lists.
# (4) The "Nested comprehensions using "enumerate" function" is displaying the results.

# Before we can perform any meaningful analysis, we need to decide what we are trying to measure
# Section (1) and (2) displays the results while section (3) creates a complete list.

# So we will start by measuring how fast the results can be displayed (1) and (2) and (4)
# So we will comment out section (3) "using Nested comprehensions"

# =============================================================
# timeit module: Measure execution time of small code snippets
# =============================================================
# This module provides a simple way to time small bits of Python code.
# It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.

# The instructions here show you how to test single lines of code, but it gets more complex when testing larger code.
# Remember indentations are vital in python, so you need to start strings with correct number of spaces.
# https://docs.python.org/3/library/timeit.html

# We are not going to use "command line" here but will use "timeit module".
# We import "timeit module".
# Then either we use "timeit function" or create an instance of the "timeit class".

# The "timeit function" is one of the three convenient functions that make use of the timeit class a bit easier.
# Here we will use the "timeit function" because printing the results is slightly easier.
# See section "28.5.2 Python interface" from link above.

# Here is the timeit function:
# timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)

# The parameters to pass to it are:
# "stmt" - can pass statement as a string, but you can also pass a function instead as long as it does not
# "setup" - Then pass the setup code (setup), we will look at this later
# "timer" - Then pass the "timer", we can use default (which comes from time.conf) or change it if we like, although its rarely changed.
# "number" - Number specifies how many times to execute the code. default is 1000000, but you can change it
# "globals" - This is used to specify the namespace that the code will run in. We will explain it in example below

# First we import timeit module
# VITAL: if you are importing a module, say "timeit" and your filename is called "timeit1.py", you will have conflict and get error
# Error message: TypeError: 'module' object is not callable
# When you hover over "import timeit" (or whatever you are importing that has conflict), it says "import resolves to its containing file"
# Solution is to change your .py filename so it does not have conflict.

import timeit

locations = {0: "Beginning",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


# We have two choices about using timeit.
# (1) We can turn our three sections of code into functions, or
# (2) Wrap them in quotes to turn them into strings.

# We are going to use (2) i.e. Wrap them in quotes and turn them into strings.
# NOTE that when using strings, you use triple quotes """   """
# That way, any reformatting of your code can be kept to a minimum.

# First string test is between LINE_5 and LINE_6 to test how long it takes for the code between them to run.
# NOTE that the \ after """ in LINE_5 is a line continuation character put there because we don't want the line to start with blank line.
# NOTE: make sure code is indented properly, otherwise timeit will give error.

# Second string test is between LINE_7 and LINE_8
# Third string test is between LINE_9 and LINE_10

# Now we have three strings to pass to the "timeit" function to see how their perfomance compares.

# Starting LINE_11
# Then we will call the timeit module's timeit function and pass it the test strings so it calculates the time to run that code section
# Go to section under LINE_11 for more explanation



# ========================
# using nested for loops
# ========================

print("nested for loops:")
print("-----------------")

# add LINE_5 below. Make sure there is no space after \. otherwise you get SyntaxError: unexpected character after line continuation character
nested_for_loop_time = """\
for loc in sorted(locations):
    exits_to_destination_1 = []   # LINE_1: New list created each time through the loop
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)
"""  # LINE_6: ADD these closing """ here

print("="*20)


# Results:

# nested for loops:
# -----------------
# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]


# =============================================
# using list comprehension inside a for loops:
# =============================================

print("Using List comprehension inside a for loop:")
print("-------------------------------------")

# LINE_7 starts below
list_comprehension_inside_for_loop_time = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]  # LINE_2
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)
"""  # LINE_8

print("="*20)

# Results:

# Using List comprehension inside a for loop:
# -------------------------------------
# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]


# =============================
# using Nested comprehensions:
# =============================
# This one produces a list with all the above exits to each location.
# We will format it in next section.


print("Using Nested Comprehensions:")
print("----------------------------")

exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
print(exits_to_destination_3)
print("="*20)

# Results:
# all in one line

# Using Nested Comprehensions:
# ----------------------------
# [[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')], [(3, 'Building'),
# (4, 'Valley'), (5, 'Forest')], [(1, 'Road'), (4, 'Valley'), (5, 'Forest')], [(1, 'Road')], [(1, 'Road')], [(1, 'Road'), (2, 'Hill')]]


# ====================================================
# Nested comprehensions using "enumerate" function:
# ====================================================

# We can use the enumerate function to get the index of each list in the other list

print("nested comprehension using enumerate:")
print("------------------------")

# LINE_9 starts below
nested_comp_using_enumerate_time = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
for index, loc in enumerate(exits_to_destination_3):  # unpacking exits_to_destination_3 into index and loc
    print("Locations leading to {}".format(index), end='\t')
    print(loc)
"""   # LINE_10

print("="*20)


# Results

# format using enumerate:
# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]

# ==============================================

# LINE_11

# If you use the calling code as follows, you get error message:
# NameError: name 'locations' is not defined

# This is because timeit is not aware of anything that is defined in your program except the arguments we passed to it inside of """ """
# This is why we have "setup" and "global" parameters to allow us to setup the environment that our code will execute in.
# NOTE: We use "setup" whenever possible because it allows us to be more specific about what you pass to them.

# result_1 = timeit.timeit(nested_for_loop_time)
# print("nested_for_loop_time = {}".format(result_1))

# ===============
# using "globals
# ===============

# We will first start with using "globals" here because it is easier
# We have already seen how to get the global variables for our modules earlier using "globals function"
# So we can pass the results of calling "globals" as the "globals argument" and pass it to "timeit"

# Our code snippet will now execute in our global namespace which means that everything defined in our module will be available to the snippet.
# That can be overkill when testing small code, but it can be useful if the environment is too complex to setup in a small block of code.
# Another reason to not use "globals" to set namespace is because it was introduced in python 3.5 and will not work in earlier versions.

# NOTE that the default "number" of runs in timeit is 1000000 times. This will take a long time, so we will change "number" to 1000

# After we run this code, it gives results below, showing the number of seconds it takes to run snippets of code 1000 times
# We can then compare them to see which code snippet runs fastest.
# From results below, looks like Code 1 and 3 are taking similar time, and code 2 is slower.

result_1 = timeit.timeit(nested_for_loop_time, globals=globals(), number=1000)  # globals is assigned call to globals function and passed to timeit.
result_2 = timeit.timeit(list_comprehension_inside_for_loop_time, globals=globals(), number=1000)
result_3 = timeit.timeit(nested_comp_using_enumerate_time, globals=globals(), number=1000)

print("="*30)
print("nested_for_loop_time:                    = {}".format(result_1))
print("list_comprehension_inside_for_loop_time: = {}".format(result_2))
print("nested_comp_using_enumerate_time:        = {}".format(result_1))
print("="*30)

# Results 1:
# nested_for_loop_time:                    = 0.13431248958537098
# list_comprehension_inside_for_loop_time: = 0.1651983549112372
# nested_comp_using_enumerate_time:        = 0.13431248958537098

# Results 2:
# nested_for_loop_time:                    = 0.15543396098830906
# list_comprehension_inside_for_loop_time: = 0.17928738580132872
# nested_comp_using_enumerate_time:        = 0.15543396098830906



# ===============
# using "setup"
# ===============

# Go to "timeit2.py" to see how to use "setup"



