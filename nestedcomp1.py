
# ==================
# nestedcomp1.py
# ==================

# ==================================
# Nested  Comprehensions
# ==================================

# it is common to next one "for loop" inside another and you can also nest "for loop" inside comprehensions
# This is called nested comprehensions

burgers = ["beef", "chicken", "Veges"]
toppings = ["cheese", "eggs", "beans", "spam"]

# Nested comprehension to print a burger with each topping
meals = [(burger, topping) for burger in burgers for topping in toppings]  # has two for loops one nested in another
print(meals)
print("="*20)

# Equivalent for loop to print a burger with each topping
meals = []
for burger in burgers:
    for topping in toppings:
        meals.append((burger, topping))   # Remember double quotes because it is a tuple
print(meals)
print("="*20)

# Results for above both is similar:

# [('beef', 'cheese'), ('beef', 'eggs'), ('beef', 'beans'), ('beef', 'spam'), ('chicken', 'cheese'), ('chicken', 'eggs'), ('chicken', 'beans'), ('chicken', 'spam'), ('Veges', 'cheese'), ('Veges', 'eggs'), ('Veges', 'beans'), ('Veges', 'spam')]
# ====================
# [('beef', 'cheese'), ('beef', 'eggs'), ('beef', 'beans'), ('beef', 'spam'), ('chicken', 'cheese'), ('chicken', 'eggs'), ('chicken', 'beans'), ('chicken', 'spam'), ('Veges', 'cheese'), ('Veges', 'eggs'), ('Veges', 'beans'), ('Veges', 'spam')]


# ========================================================
# NOTE: you can modify above programs to print each individual meal with toppings in its own line


# Nested comprehension to print a burger with each topping

for meals in [(burger, topping) for burger in burgers for topping in toppings]:  # has two for loops one nested in another
    print(meals)
print("="*20)

# Equivalent for loop to print a burger with each topping

for burger in burgers:
    for topping in toppings:
        print((burger, topping))
print("="*20)


# Results for both above:

# ====================
# ('beef', 'cheese')
# ('beef', 'eggs')
# ('beef', 'beans')
# ('beef', 'spam')
# ('chicken', 'cheese')
# ('chicken', 'eggs')
# ('chicken', 'beans')
# ('chicken', 'spam')
# ('Veges', 'cheese')
# ('Veges', 'eggs')
# ('Veges', 'beans')
# ('Veges', 'spam')
# ====================
# ('beef', 'cheese')
# ('beef', 'eggs')
# ('beef', 'beans')
# ('beef', 'spam')
# ('chicken', 'cheese')
# ('chicken', 'eggs')
# ('chicken', 'beans')
# ('chicken', 'spam')
# ('Veges', 'cheese')
# ('Veges', 'eggs')
# ('Veges', 'beans')
# ('Veges', 'spam')
# ====================

# =====================================================================================
# NOTE: We have used a comprehension to combine two existing lists to produce another list
# containing all combinations.
# It is not recommended to do that in this case because we are producing what is called
# a "product" of the two lists and python has a function to do that in the standard library.
# We will look at that later.

# =====================================================================================
# NOTE: that if you are going to iterate over a list and don't intend to use it again
# You should consider using a "Generator expression" instead
# We will explain this later on.
# But in above code, we have used a "Nested Comprehension" in place of "for loops"
# =====================================================================================



# =================================================
# Other ways of writing nested list comprehensions:
# =================================================

# you can write nested list comprehensions in a different way to get different results.

# Original nested list comprehension
# This produces a list that holds all the tuples
# See diagram named "nestedcomp1_A" for diagram of logic

for meals in [(burger, topping) for burger in burgers for topping in toppings]:  # has two for loops one nested in another
    print(meals)
print("="*20)

# Results:

# ('beef', 'cheese')
# ('beef', 'eggs')
# ('beef', 'beans')
# ('beef', 'spam')
# ('chicken', 'cheese')
# ('chicken', 'eggs')
# ('chicken', 'beans')
# ('chicken', 'spam')
# ('Veges', 'cheese')
# ('Veges', 'eggs')
# ('Veges', 'beans')
# ('Veges', 'spam')

# ============================
# Modified
# This produces four lists, each containing the tuples

# See diagram named "nestedcomp1_B" for diagram of logic

burgers = ["beef", "chicken", "veges"]
toppings = ["cheese", "eggs", "beans", "spam"]

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:  # modified to add extra [ at start and ] before burgers
    print("meals = {}".format(nested_meals))
print("="*20)

# Results:

# ====================
# meals = [('beef', 'cheese'), ('chicken', 'cheese'), ('veges', 'cheese')]
# meals = [('beef', 'eggs'), ('chicken', 'eggs'), ('veges', 'eggs')]
# meals = [('beef', 'beans'), ('chicken', 'beans'), ('veges', 'beans')]
# meals = [('beef', 'spam'), ('chicken', 'spam'), ('veges', 'spam')]

# ================================================
# Here is another way of modifying above program
# ================================================
# We are going to change the order of for loop and bring toppings inside the []

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:  # modified to add extra [ at start and ] before burgers
    print("meals = {}".format(nested_meals))
print("="*20)

# Results:

# meals = [('beef', 'cheese'), ('beef', 'eggs'), ('beef', 'beans'), ('beef', 'spam')]
# meals = [('chicken', 'cheese'), ('chicken', 'eggs'), ('chicken', 'beans'), ('chicken', 'spam')]
# meals = [('veges', 'cheese'), ('veges', 'eggs'), ('veges', 'beans'), ('veges', 'spam')]


