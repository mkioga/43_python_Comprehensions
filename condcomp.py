
# ===============
# condcomp.py
# ===============


# =============================
# Conditional comprehensions:
# =============================

# It is very common to have an "if clause" in a "for loop" and we can have an "if clause" in comprehensions too

# We are going to use this code we had used in a previous section.
# It has a list with food that we will try to choose from

# SECTION_1:
# We are using a for loop and it chooses the meal that does not contain "spam"

# SECTION_2: (Conditional comprehension)
# Comprehension with filter (if clause)
# We will use comprehension to choose meals that don't contain "spam" by adding "if clause' to the comprehension.

# Conditional comprehension have three sections: Expression, iteration and filter(s)
# <<= Expression <<=====> Iteration <<==========>>Filter(s)
# <<=== meal <<====>> for meal in menu <<===>> if spam not in meal
# [meal for meal in menu if "spam" not in meal]  (Here is example from SECTION_2)


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

# SECTION_1: chooses meal using for loop.

print("Meals using for loop:")
for meal in menu:
    if "spam" not in meal:
        print(meal)
print("="*20)

# Result:

# chooses only meal with no spam

# ['egg', 'sausage', 'bacon']
# ['chicken', 'chips']

# =================================================
# We will print this as a list for results to match one below from comprehension

print("Meals using for loop but appended to create a list:")
meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)

print(meals)
print("="*20)

# Results:

# Meals using for loop but appended to create a list:
# [['egg', 'sausage', 'bacon'], ['chicken', 'chips']]


# =============================================

# SECTION_2:
# We use comprehension to choose meal that does not have "spam" by including "if clause" in the comprehension.

# Conditional comprehension have three sections: Expression, iteration and filter(s)
# <<= Expression <<=====> Iteration <<==========>>Filter(s)
# <<=== meal <<====>> for meal in menu <<===>> if spam not in meal
# [meal for meal in menu if "spam" not in meal]  (example here)

# NOTE that the if section here acts as a filter
# The meal is included in meal if the condition is true (i.e. it does not have spam) otherwise it is skipped

print("Meals using comprehension_1:")
meals = [meal for meal in menu if "spam" not in meal]
print(meals)
print("="*20)

# Results:

# We get the meals with no spam in a list (enclosed in [ ] )

# [['egg', 'sausage', 'bacon'], ['chicken', 'chips']]


# ========================================
# For loop also showing skipped meals:
# ========================================

# We will use "else clause" to show when meal was skipped.

print("Using for loop to also show when meal is skipped:")
meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("Meal Skipped")

print(meals)
print("="*20)

# Results:

# Using for loop to also show when meal is skipped:
# ['Meal Skipped', ['egg', 'sausage', 'bacon'], 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', 'Meal Skipped', ['chicken', 'chips']]


# =================================================
# Using comprehension to show when meal is skipped:
# =================================================

# Since the "if clause" in comprehension already filters the meal that is chosen,
# we cannot use "else clause" in the comprehension because the results let in are already filtered.
# NOTE: We get error if we try to add else clause: LINE_1 here
# We will see how to deal with this later on.


# print("Using comprehension to show when meal is skipped:")
# # meals = [meal for meal in menu if "spam" not in meal else ]  # LINE_1: We get error if we try to add else clause in comprehension
# print(meals)
# print("="*20)


# ========================================================
# Complex filters in comprehensions: using two if clauses
# ========================================================

# Say we want a meal that does not have "spam" and "chicken"
# we can use two "if clauses" to exclude both "spam" and "chicken"
# We can see here we are excluding both spam and chicken.

print("Using multiple 'if' clauses in comprehensions:")
meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
print(meals)
print("="*20)

# Results:

# Using to if clauses in comprehensions:
# [['egg', 'sausage', 'bacon']]


# ========================================================
# Complex filters in comprehensions: using "if" & "and"
# ========================================================

# We can do the same filter above by using "if" & "and" instead of two "if" clauses
# Results are the same. We exclude both spam and chicken

print("Using to 'if' & 'and' clauses in comprehensions:")
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)
print("="*20)

# Results:

# Using to 'if' & 'and' clauses in comprehensions:
# [['egg', 'sausage', 'bacon']]



# ================================================
# More complex filters in comprehensions:
# ================================================

# Say a customer wants "spam" or "eggs" in meal but does not want "bacon" and "sausage" in meal.
# Here are two ways of writing this condition.
# NOTE: The results here show spam and eggs are chosen, but it is not eliminating bacon and sausage as we expected.

print("Allow spam & eggs but no bacon and sausage:")
fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
print("="*10)
fussy_meals = [meal for meal in menu if ("spam" in meal or "egg" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
print("="*20)

# Results:

# Allow spam & eggs but no bacon and sausage:
# [['egg', 'spam', 'bacon'], ['egg', 'spam'], ['egg', 'bacon', 'spam'], ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'], ['spam', 'egg', 'sausage', 'spam']]
# ==========
# [['egg', 'spam', 'bacon'], ['egg', 'spam'], ['egg', 'bacon', 'spam'], ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'], ['spam', 'egg', 'sausage', 'spam']]


# =============================================================================================
# My correction of above code to filter out "bacon" and "sausage" and include "egg" or "spam":
# =============================================================================================

# This filter works if you put "if not" first, then put "if" second.

fussy_meals = [meal for meal in menu if not "bacon" in meal if not "sausage" in meal if "egg" in meal if "spam" in meal]
print(fussy_meals)
print("="*20)

# Results:

# [['egg', 'spam']]

# ==============================
# This "if not" in brackets does not filter out bacon and sausage

fussy_meals = [meal for meal in menu if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
print("="*20)

# Results:

# [['egg', 'spam', 'bacon'], ['egg', 'spam'], ['egg', 'bacon', 'spam'], ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'], ['spam', 'egg', 'sausage', 'spam'], ['chicken', 'chips']]


# ======================================================
# This "if not" filter works. Need to have "not in" meal inside the bracket

fussy_meals = [meal for meal in menu if ("bacon" not in meal and "sausage" not in meal)]
print(fussy_meals)
print("="*20)

# Results:

# [['egg', 'spam'], ['chicken', 'chips']]


# ======================================================
# Now we will include "spam" or "eggs" and filter out "bacon" and "sausage"
# This one works with the exclusion clause coming first and then inclusion clause coming second.

fussy_meals = [meal for meal in menu if ("bacon" not in meal and "sausage" not in meal) if "spam" in meal or "sausage" in meal]
print(fussy_meals)
print("="*20)

# Results:

# [['egg', 'spam']]


# ======================================================
# Now we will include "spam" or "eggs" and filter out "bacon" and "sausage"
# This one works too with the inclusion clause coming first and then exclusion clause coming second.

fussy_meals = [meal for meal in menu if "spam" in meal or "sausage" in meal if ("bacon" not in meal and "sausage" not in meal)]
print(fussy_meals)
print("="*20)

# Results:

# [['egg', 'spam']]

# =============================================================
# so we need to have the (not in) clause inside the brackets
# =============================================================


# Now we will go to condcomp1.py to resolve the "else" issue where we could not add "else" in a comprehension.







