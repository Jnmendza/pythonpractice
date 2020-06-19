import math
from math import sqrt

# To analyze
# 1. does # of steps increase if input size increases?
# 2. go line by line. Figure out big-O of each line and add
# 3. If you have a loop: look inside and repeat step 2
#    3.2 - calculate how many times the loop will run
#    3.3 - result of 3.1 X (multiplied) result of 3.2

# Constant time == O(1)
def mult_2(n):
    return n * 2


# Linear time == O(n)
# The loop is running n amount of times (3.2)
def foo(n):
    for i in range(0, n):
        print(i)


# Quadratic time (Polynomial Time)
def bar(n): # O(1) + O(n^2) + O(1) ==> O(n^2)
    s = 0 # O(1)

    # O(n) * O(n) = O(n^2)
    for i in range(0, n): # O(n)
        for j in range(0, n): # O(n) * O(1) = O(n) this loop runs in linear time
            s += i * j

    return s # O(1)


# O(n) * O(sqrt(n)) == n * sqrt n
# also a variant of O(n) * log(n)
def baz(n):
    s = 0

    for i in range(n):
        for j in range(int(sqrt(n))): # O(sqrt(n))
            s += i * j # O(1)

    return s


# Logarithmic log(n)
# When the input is halved every step of the loop
def divider(n):
    while n >= 0:
        print(n) # O(1)
        n = n//2 # O(1)