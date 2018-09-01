
# ==========
# timeit3
# ==========

# ======================================
# Passing code to timeit as a function
# ======================================


# It is important to pay attention to what you are timing and under what conditions under which the code is running.
# in our earlier examples, printing the output was affecting the timing results
# We will modify our code so that all three of our code snippets start doing the same thing.
# We will also defer the printing until after the lists have been created so printing does not interfere with the results.

# We will also see how to pass the code to timeit as a function

# When you run this program, it works. See results below

import timeit

# We leave this code as string here

setup = """\
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
"""


# We define the dictionaries here.

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

# We turn the code into functions

def nested_for_loop_time():
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        print("Locations leading to {}".format(loc), end='\t')
        print(exits_to_destination_1)

def list_comprehension_inside_for_loop_time():
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)

def nested_comp_using_enumerate_time():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
    for index, loc in enumerate(exits_to_destination_3):
        print("Locations leading to {}".format(index), end='\t')
        print(loc)


# NOTE: We pass a reference to the function rather than a string containing the code snippets
# NOTE that this will only work with functions that don't take any arguments.
# If you need to pass arguments to your functions, then you cannot pass functions directly to timeit function
# We will see a way around that by using "decorators". We will cover that later.


result_1 = timeit.timeit(nested_for_loop_time, setup, number=1000)
result_2 = timeit.timeit(list_comprehension_inside_for_loop_time, setup, number=1000)
result_3 = timeit.timeit(nested_comp_using_enumerate_time, setup, number=1000)

print("="*30)
print("nested_for_loop_time:                    = {}".format(result_1))
print("list_comprehension_inside_for_loop_time: = {}".format(result_2))
print("nested_comp_using_enumerate_time:        = {}".format(result_3))



# Results:

# nested_for_loop_time:                    = 0.9182593502237485
# list_comprehension_inside_for_loop_time: = 0.22603669330396714
# nested_comp_using_enumerate_time:        = 0.9182593502237485




# ======================
# Timing without print:
# ======================

# Now we will make changes so that all three functions create the same list
# and don't do any printing

# We will start from CHANGE_1



import timeit

# We leave this code as string here

setup = """\
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
"""


# We define the dictionaries here.

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

# We turn the code into functions

def nested_for_loop_time():
    result = []   # CHANGE_1: Create an empty list
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)  # CHANGE_2: We append to results and delete the prints below
    return result       # CHANGE_3: Then we return the result
        # print("Locations leading to {}".format(loc), end='\t')  # Remove these prints
        # print(exits_to_destination_1)

def list_comprehension_inside_for_loop_time():
    result = []    # CHANGE_4: We create an empty list
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)  # CHANGE_5
    return result       # CHANGE_6
    # print("Locations leading to {}".format(loc), end='\t')
    # print(exits_to_destination_2)

def nested_comp_using_enumerate_time():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
    return exits_to_destination_3   # CHANGE_7: Here we just return exits_to_destination_3 and delete below for loop
    # for index, loc in enumerate(exits_to_destination_3):
    #     print("Locations leading to {}".format(index), end='\t')
    #     print(loc)



# We will print out the results to make sure the code snippets are doing the same thing

print("="*30)
print(nested_for_loop_time())
print(list_comprehension_inside_for_loop_time())
print(nested_comp_using_enumerate_time())


# NOTE: We pass a reference to the function rather than a string containing the code snippets
# NOTE that this will only work with functions that don't take any arguments.
# If you need to pass arguments to your functions, then you cannot pass functions directly to timeit function
# We will see a way around that by using "decorators". We will cover that later.


result_1 = timeit.timeit(nested_for_loop_time, setup, number=1000)
result_2 = timeit.timeit(list_comprehension_inside_for_loop_time, setup, number=1000)
result_3 = timeit.timeit(nested_comp_using_enumerate_time, setup, number=1000)

print("="*30)
print("nested_for_loop_time:                    = {}".format(result_1))
print("list_comprehension_inside_for_loop_time: = {}".format(result_2))
print("nested_comp_using_enumerate_time:        = {}".format(result_1))


# When we run above code, we see all three functions are printing the same thing.
# But they have different times, but the difference is very small.
# NOTE that the results of timing have smaller values because we are not timing the print.


# Results:

# ==============================
# [[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')], [(3, 'Building'),
# (4, 'Valley'), (5, 'Forest')], [(1, 'Road'), (4, 'Valley'), (5, 'Forest')], [(1, 'Road')], [(1, 'Road')], [(1, 'Road'), (2, 'Hill')]]
#
# [[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')], [(3, 'Building'),
# (4, 'Valley'), (5, 'Forest')], [(1, 'Road'), (4, 'Valley'), (5, 'Forest')], [(1, 'Road')], [(1, 'Road')], [(1, 'Road'), (2, 'Hill')]]
#
# [[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')], [(3, 'Building'),
# (4, 'Valley'), (5, 'Forest')], [(1, 'Road'), (4, 'Valley'), (5, 'Forest')], [(1, 'Road')], [(1, 'Road')], [(1, 'Road'), (2, 'Hill')]]
# ==============================
# nested_for_loop_time:                    = 0.03921273857047293
# list_comprehension_inside_for_loop_time: = 0.044275153895010876
# nested_comp_using_enumerate_time:        = 0.03921273857047293





# ===========================================
# Generators vs List comprehensions
# ===========================================

# Now we will check if there is any difference in performance when using Generators vs list comprehensions
# Note that generators are enclosed in ( )
# List comprehensions are enclosed in [ ]

# In this case, we will test nested_comp_using_enumerate_time when coded in both generators and list comprehensions

# From the result below, we see that Nexted Gen (using generator) is more than 10 times faster than using list comprehension
# This is because the generator is not spending time building up the list, it just returns each one when we iterate over it.

# NOTE that even if using generator is much faster to build up loops or list comprehensions, we will pay for it when
# we come to iterate over the generator.

# We will add the same loop to each of our functions in the next section to test this.

import timeit

# We leave this code as string here

setup = """\
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
"""


# We define the dictionaries here.

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

# We turn the code into functions

def nested_for_loop_time():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
    return result


def list_comprehension_inside_for_loop_time():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
    return result

# Using list comprehension

def nested_comp_using_enumerate_time():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
    return exits_to_destination_3

# Using generator. See line CHANGE_1 is enclosed in () instead of []

def nested_gen_comp_using_enumerate_time():
    exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations))  # CHANGE_1
    return exits_to_destination_3

# We will print out the results to make sure the code snippets are doing the same thing

print("="*30)
print(nested_for_loop_time())
print(list_comprehension_inside_for_loop_time())
print(nested_comp_using_enumerate_time())
# print(nested_gen_comp_using_enumerate_time())   # We print the generator here

# NOTE: We pass a reference to the function rather than a string containing the code snippets
# NOTE that this will only work with functions that don't take any arguments.
# If you need to pass arguments to your functions, then you cannot pass functions directly to timeit function
# We will see a way around that by using "decorators". We will cover that later.


result_1 = timeit.timeit(nested_for_loop_time, setup, number=1000)
result_2 = timeit.timeit(list_comprehension_inside_for_loop_time, setup, number=1000)
result_3 = timeit.timeit(nested_comp_using_enumerate_time, setup, number=1000)
result_4 = timeit.timeit(nested_gen_comp_using_enumerate_time, setup, number=1000)  # We time the generator here


print("="*30)
print("nested_for_loop_time:                    = {}".format(result_1))
print("list_comprehension_inside_for_loop_time: = {}".format(result_2))
print("nested_comp_using_enumerate_time:        = {}".format(result_3))
print("nested_gen_comp_using_enumerate_time:    = {}".format(result_4))  # Then we print generator here


# Results

# nested_for_loop_time:                    = 0.030483166337021018
# list_comprehension_inside_for_loop_time: = 0.03318130993694471
# nested_comp_using_enumerate_time:        = 0.027145051330536782
# nested_gen_comp_using_enumerate_time:    = 0.0018915381290134092  # Nested_gen is much faster





# =====================================================
# Generators vs List comprehensions with iterations
# =====================================================

# NOTE that even if using generator is much faster to build up loops or list comprehensions, we will pay for it when
# we come to iterate over the generator.

# We will add the same loop to each of our functions here named LOOP_SECTION

# When we run the code, we see that the time is almost same for all,
# including last two where there was list comprehension and generator
# So whatever time you saved with generator was used up in the loop


import timeit

# We leave this code as string here

setup = """\
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
"""


# We define the dictionaries here.

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

# We turn the code into functions

def nested_for_loop_time():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
    # Print the result before returning. LOOP_SECTION
    for x in result:
        pass

    return result


def list_comprehension_inside_for_loop_time():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
    # Print the result before returning. LOOP_SECTION
    for x in result:
        pass

    return result

# Using list comprehension

def nested_comp_using_enumerate_time():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
    # Print the result before returning. LOOP_SECTION
    for x in exits_to_destination_3:  # we use exits_to_destination_3 instead of result
        pass

    return exits_to_destination_3

# Using generator. See line CHANGE_1 is enclosed in () instead of []

def nested_gen_comp_using_enumerate_time():
    exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations))  # CHANGE_1
    # Print the result before returning. LOOP_SECTION
    for x in exits_to_destination_3:  # we use exits_to_destination_3 instead of result
        pass

    return exits_to_destination_3

# We will print out the results to make sure the code snippets are doing the same thing

print("="*30)
print(nested_for_loop_time())
print(list_comprehension_inside_for_loop_time())
print(nested_comp_using_enumerate_time())
# print(nested_gen_comp_using_enumerate_time())   # We print the generator here

# NOTE: We pass a reference to the function rather than a string containing the code snippets
# NOTE that this will only work with functions that don't take any arguments.
# If you need to pass arguments to your functions, then you cannot pass functions directly to timeit function
# We will see a way around that by using "decorators". We will cover that later.


result_1 = timeit.timeit(nested_for_loop_time, setup, number=1000)
result_2 = timeit.timeit(list_comprehension_inside_for_loop_time, setup, number=1000)
result_3 = timeit.timeit(nested_comp_using_enumerate_time, setup, number=1000)
result_4 = timeit.timeit(nested_gen_comp_using_enumerate_time, setup, number=1000)  # We time the generator here


print("="*30)
print("nested_for_loop_time:                    = {}".format(result_1))
print("list_comprehension_inside_for_loop_time: = {}".format(result_2))
print("nested_comp_using_enumerate_time:        = {}".format(result_3))
print("nested_gen_comp_using_enumerate_time:    = {}".format(result_4))  # Then we print generator here


# Results


# nested_for_loop_time:                    = 0.03613664959271254
# list_comprehension_inside_for_loop_time: = 0.0344986850398835
# nested_comp_using_enumerate_time:        = 0.033191573629314075
# nested_gen_comp_using_enumerate_time:    = 0.03970116957793282