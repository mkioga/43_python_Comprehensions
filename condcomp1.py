
# ===============
# condcomp1.py
# ===============

# =======================================
# Conditional Expressions:
# =======================================

# SECTION_1: when using for loop, we are able to use "else" clause to print "Meal Skipped" Whenever a meal is skipped

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# SECTION_1:

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("Meal skipped")
print(meals)
print("="*20)

# Results:

# ['Meal skipped', ['egg', 'sausage', 'bacon'], 'Meal skipped', 'Meal skipped', 'Meal skipped', 'Meal skipped', 'Meal skipped', 'Meal skipped', ['chicken', 'chips']]

# ===============================================
# This Comprehension only shows the meals that are chosen

meals = [meal for meal in menu if "spam" not in meal]
print(meals)
print("="*20)

# Results:

# [['egg', 'sausage', 'bacon'], ['chicken', 'chips']]



# ==================================
# Using Conditional Expression:
# ==================================

# Now we will try to make a comprehension that will produce same list as the for loop above (with "Meal Skipped")

# DEFINITION: A Conditional Expression is a condition that we can assign to something of use anywhere else that an expression is needed

# Below is an example of a conditional expression
# NOTE: A Conditional Expression must have an "else" clause

# Expression. assign "Twelve" to variable expression if x equals 12, else assign "unknown"
# If x = 12, expression gets "Twelve" and if x = 15, expression gets "unknown"

x = 12
expression = "Twelve" if x == 12 else "unknown"  # Expression needs an else clause otherwise you get an error
print("expression1 = {}".format(expression))
print("="*20)

# Result:

# expression1 = Twelve

x = 15
expression = "Twelve" if x == 12 else "unknown"  # Expression needs an else clause otherwise you get an error
print("expression1 = {}".format(expression))
print("="*20)

# Result:

# expression1 = unknown

# =========================================================
# Using Conditional Expression to resolve our "else" issue
# =========================================================

# We want an Expression that evaluates to the meal if the meal does not contain "spam"
# Otherwise it evaluates to the string saying "Meal Skipped"

# Here is the original for loop with its else clause.

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("Meal skipped")
print(meals)
print("="*20)

# Results:

# ['Meal skipped', ['egg', 'sausage', 'bacon'], 'Meal skipped', 'Meal skipped', 'Meal skipped', 'Meal skipped', 'Meal skipped', 'Meal skipped', ['chicken', 'chips']]


# ==============================
# Using Conditional Expression:
# ==============================

# This one gives same results as the for loop with else.
# If we compare this with conditional expression: expression = "Twelve" if x == 12 else "unknown"

# We see the following corresponding:

# Expression Part:

# "meal" ==> "Twelve"
# "if "spam" not in meal ==> "if x == 12"
# "else "Meal Skipped" ==> "else "unknown"

# NOTE that you can also use a function in the Expression part to avoid excessively complex code.

# Iteration Part:
# Then "for meal in menu" is the iteration part.


# Remember Conditional comprehension have three sections: Expression, iteration and filter(s)
# <<= Expression <<=====> Iteration <<==========>>Filter(s)
# <<=== meal <<====>> for meal in menu <<===>> if spam not in meal
# [meal for meal in menu if "spam" not in meal]


meals = [meal if "spam" not in meal else "Meal Skipped" for meal in menu]
print(meals)
print("="*20)

# Results:

# ['Meal Skipped', ['egg', 'sausage', 'bacon'], 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', ['chicken', 'chips']]



# ===============================================
# More complex Conditional Expressions
# ===============================================

# In this for loop, we print "contains egg" as the default if we don't find sausage and bacon.
# so last result gives error because it only has chicken and chips but says contains egg
# So this program is obviously not having correct logic

# To correct it, we would need to test for membership in a "list" or "set"
# We will do this in next section

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")
print("="*20)

# Results:

# ['egg', 'spam', 'bacon'] contains bacon
# ['egg', 'sausage', 'bacon'] contains sausage
# ['egg', 'spam'] contains egg
# ['egg', 'bacon', 'spam'] contains bacon
# ['egg', 'bacon', 'sausage', 'spam'] contains sausage
# ['spam', 'bacon', 'sausage', 'spam'] contains sausage
# ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'] contains bacon
# ['spam', 'egg', 'sausage', 'spam'] contains sausage
# ['chicken', 'chips'] contains egg

# ================================
# Print whole menu for reference
# ================================
print(menu)
print("="*20)

# Results:

# [['egg', 'spam', 'bacon'], ['egg', 'sausage', 'bacon'], ['egg', 'spam'], ['egg', 'bacon', 'spam'], ['egg', 'bacon', 'sausage', 'spam'], ['spam', 'bacon', 'sausage', 'spam'], ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'], ['spam', 'egg', 'sausage', 'spam'], ['chicken', 'chips']]


# ========================================
# Testing for membership in set
# ========================================

# # ===========================
# # code with print to verify:
# # ===========================
#
# # print(items) prints only the unique meal items in the meal.
# # on LINE_1, the items.add(item) adds any new item that is not already in the items
#
# items = set()
# print("initial items = {}".format(items))
#
# for meal in menu:  # iterates through menu and gets one meal at a time
#     print("meal  = {}".format(meal))  # meal is a list containing whole meal e.g. ['egg', 'spam', 'bacon'] is the first meal
#     for item in meal:  # iterates through the meal above to get items: egg, spam and bacon
#         print("item = {}".format(item))  # Prints the items one at a time
#         items.add(item)  # Then adds the items to the items set: LINE_1: add does not duplicate
#         print("New items = {}".format(items))  # Prints new items with the item added to it. NOTE: it does not duplicate.
#
# print("Final items = {}".format(items))  # Prints the final list in items
# print("="*20)

# ============================
# Code above without prints:
# ============================

# This code produces items list which has all items in the meals.
# There is no duplication

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print("="*20)


# Results:
# {'bacon', 'sausage', 'chicken', 'chips', 'spam', 'egg'}

# # ==============================
# # Now we use the "items" set to check against the meals to see what is in the meal
# # ==============================
#
# for meal in menu:
#     print("meal = {}".format(meal))    # Initial meal is: ['egg', 'spam', 'bacon']
#     print("items = {}".format(items))  # Items list to check against is: {'egg', 'spam', 'chips', 'chicken', 'sausage', 'bacon'}
#
#     for item in items:  # iterates through items list above, starting with egg
#         print("item = {}".format(item))  # First item in items list above is egg
#
#         if item in meal:  # Checks if item (egg) is in meal ['egg', 'spam', 'bacon']. This is true
#             print("{} contains {}".format(meal, item))  # If true, prints: meal contains the item e.g. ['egg', 'spam', 'bacon'] contains egg
#             print("="*10)
#             break  # It breaks if meal does not contain the item. Then goes back to meal again to check next meal for this item
# print("="*20)
#
#
# # Results:
#
# # meal = ['egg', 'spam', 'bacon']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['egg', 'spam', 'bacon'] contains egg
# # ==========
# # meal = ['egg', 'sausage', 'bacon']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['egg', 'sausage', 'bacon'] contains egg
# # ==========
# # meal = ['egg', 'spam']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['egg', 'spam'] contains egg
# # ==========
# # meal = ['egg', 'bacon', 'spam']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['egg', 'bacon', 'spam'] contains egg
# # ==========
# # meal = ['egg', 'bacon', 'sausage', 'spam']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['egg', 'bacon', 'sausage', 'spam'] contains egg
# # ==========
# # meal = ['spam', 'bacon', 'sausage', 'spam']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # item = sausage
# # ['spam', 'bacon', 'sausage', 'spam'] contains sausage
# # ==========
# # meal = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'] contains egg
# # ==========
# # meal = ['spam', 'egg', 'sausage', 'spam']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # ['spam', 'egg', 'sausage', 'spam'] contains egg
# # ==========
# # meal = ['chicken', 'chips']
# # items = {'egg', 'sausage', 'bacon', 'spam', 'chips', 'chicken'}
# # item = egg
# # item = sausage
# # item = bacon
# # item = spam
# # item = chips
# # ['chicken', 'chips'] contains chips
# # ==========


# =============================
# Above code without prints:
# =============================

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break
print("="*20)


# Results:

# ['egg', 'spam', 'bacon'] contains spam
# ['egg', 'sausage', 'bacon'] contains bacon
# ['egg', 'spam'] contains spam
# ['egg', 'bacon', 'spam'] contains spam
# ['egg', 'bacon', 'sausage', 'spam'] contains spam
# ['spam', 'bacon', 'sausage', 'spam'] contains spam
# ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'] contains spam
# ['spam', 'egg', 'sausage', 'spam'] contains spam
# ['chicken', 'chips'] contains chips
# ====================

# ========================================================================
# So as we can see, conditional expressions are very useful.
# But they should only be used to resolve a specific problem.
# ========================================================================

# ===============================================
# Using conditional expression to play fizzbuzz:
# ===============================================

# In fizzbuzz, if a number is divisible by 3, we say fizz
# if divisible by 5, we say buzz
# And if divisible by 3 and 5, we say fizz buzz (i.e. divisible by 15)
# Otherwise, we say the number


# We will put this in a range so we get some numbers to work with:
# Note that we need to check 15 first, otherwise one of the other conditions will be true before we say fizz buzz

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)


# Results:

# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizz buzz
# 16
# 17
# fizz
# 19
# buzz
# fizz
# 22
# 23
# fizz
# buzz
# 26
# fizz
# 28
# 29
# fizz buzz
