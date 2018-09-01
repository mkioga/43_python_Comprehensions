
# ===================
# timeitchallene.py
# ===================


# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# First lets test the factorials to verify they work.
# We see they both produce same result, so they work

x = fact(50)  # Function call
print(x)
y = factorial(50)  # Function call
print(y)

# Result

# 30414093201713378043612608166064768844377641568960512000000000000
# 30414093201713378043612608166064768844377641568960512000000000000


# ==========================================================================

# NOTE that both above functions (fact and factorial) take an argument, so we cannot pass them directly to timeit function

# Now we need to test the function calls above using timeit.
# There are a few ways to do this
# Remember we need to make sure we make the functions available to timeit but using the "setup argument".
# If you are using python3.5 or above, you may use "globals" instead

# ============
# Method 1
# ============

# The easy way is to is to move the function calls to after each function, then write the whole load output in a string.
# NOTE we move the call after the function. and also use 130 instead of 50

# When you run this code, we see factorial_test takes about twice as much time as fact_test


import timeit

fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

x = fact(130)
"""

factorial_test = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

y = factorial(130)
"""

# Then we call the timeit function with each string (fact_test and factorial_test)

print(timeit.timeit(fact_test, number=10000))
print(timeit.timeit(factorial_test, number=10000))

# Result:

# 0.3440643255788119
# 0.7140462856301062


# ===============================
# Method 2: Using "setup" string
# ===============================

# The setup string can be an import.
# And we can import our own module as long as we make sure the timing code is not executed

# The easy way is to is to move the function calls to after each function, then write the whole load output in a string.
# NOTE we move the call after the function. and also use 130 instead of 50

# When you run this code, we see factorial_test takes about twice as much time as fact_test


import timeit

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result



def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# Our module can be imported but we have to make sure any code we had is not executed.
# We do this by checking our __name__ == "__main__"

# NOTE that this code will execute only if the program run as a script.
# Otherwise it will not be executed if the module is imported

# NOTE that under setup=(from __main__ is same as from timeitchallenge
# Advantage of using __main__ is that it will still work even if we rename timeitchallenge.py to something else.

# When we run this, we get result below as expected.
# NOTE: you can see below format under "def test" example in below link for timeit
# https://docs.python.org/3/library/timeit.html

if __name__ == "__main__":
    print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
    print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=10000))


# Result:

# 0.4051610675206059
# 0.8224888367251818


# ==============================================
# Method 3: Using "Repeat" instead of "Timeit"
# ==============================================

# Repeat is similar to timeit but it runs the test several times and returns a list of all the individual timeits
# The only change is we will replace "timeit.timeit" with "timeit.repeat"

# When we run the code, we see it returns two lists, each with results of timeit run three times.
# This is because timeit.repeat defaults to running the test three times.
# you can however overide the defaults by adding "repeat=x" where x is the number of times you want to repeat

import timeit

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000))
    print(timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000))
    print("="*30)
    print(timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=6))
    print(timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=6))


# Results:

# [0.3266842719178132, 0.3026799104523028, 0.30393328841458556]
# [0.7077099649585467, 0.7041170688826583, 0.7068900770622175]
# ==============================
# [0.3107827937046137, 0.29504372332949336, 0.29613831593335593, 0.29241319934988574, 0.29526469458873983, 0.2952109611404534]
# [0.704769718968028, 0.7100138620221648, 0.7038695327725737, 0.7034384576930606, 0.7375495374093477, 0.7430840825828771]






# ==============================================
# Sum, mean and other arithmetic on lists
# ==============================================

# Above result is one of the reason for the warning about not performing statistical analysis on the results.
# When you have a set of values in a list, it is very easy to calculate things like sum, average, etc

# Here we will assign the lists into variables so we can use them to calculate things.


import timeit

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# We will remove print and assign the list to variables (list1 and list2)

if __name__ == "__main__":
    list1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=6)
    list2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=6)

    # Then we can use the sum function to calculate the sum of values in the lists above.
    print("sum1 = {}".format(sum(list1)))
    print("sum2 = {}".format(sum(list2)))

    # We can also calculate the arithmetic mean by dividing the sum by the number of items in the list
    sum1 = sum(list1)
    sum2 = sum(list2)
    print("Mean1 = {}".format(sum1 / 6))
    print("Mean2 = {}".format(sum2 / 6))

# Results:

# sum1 = 2.4493559231164914
# sum2 = 4.174790681050325
# Mean1 = 0.4082259871860819
# Mean2 = 0.6957984468417209






# ===========================================================
# "Statistical analysis on lists using "statistics module"
# ===========================================================


# NOTE that there is a "statistics module" in python3 standard library and we can import that to analyze the results further
# Here we will import mean and stdev methods from statistics (standard deviation = stdev)

# For more information on statistics in python, see below link
# https://docs.python.org/3/library/statistics.html


import timeit
from statistics import mean, stdev

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# We will remove print and assign the list to variables (list1 and list2)

if __name__ == "__main__":
    list1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=6)
    list2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=6)

    # Now we can use the "mean" and "stdev" methods here

    print("Mean1 = {}".format(mean(list1)))
    print("Mean2 = {}".format(mean(list2)))

    print("Stdev1 = {}".format(stdev(list1)))
    print("Stdev2 = {}".format(stdev(list2)))

# Results:

# Mean1 = 0.30065554806909756
# Mean2 = 0.6919391978864039
# Stdev1 = 0.007874257611336926
# Stdev2 = 0.0032871661079469073

