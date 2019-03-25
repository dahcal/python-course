"""
Python3 program to calculate pi to 10000 places using Chudnovskys method
"""
import math
from time import time

# Imported code. Allows for taking the square root of a fixed point(length) number. Based on Newtons method:  https://en.wikipedia.org/wiki/Newtons_method#Square_root_of_a_number
def sqrt(n, one):
    """
    Return the square root of n as a fixed point number with the one
    passed in.  It uses a second order Newton-Raphson convgence.  This
    doubles the number of significant figures on each iteration.
    """
    # Use floating point arithmetic to make an initial guess
    floating_point_precision = 10**16
    n_float = float((n * floating_point_precision) // one) / floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * one) // floating_point_precision
    n_one = n * one
    while 1:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x

# Based on Chudnovskys algorithm https://en.wikipedia.org/wiki/Chudnovsky_algorithm
def pi_chudnovsky(one = 1000000) :
    """
    Calculate pi as an integer number of fixed length defined by one
    This is to prevent float error
    """
    # Defines of values for Chudkovskys formula
    k = 1
    a_k = one
    a_sum = one
    b_sum = 0
    C = 640320
    C3_OVER_24 = C**3 // 24
    while 1 :
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*C3_OVER_24
        a_sum += a_k
        b_sum += k*a_k
        k += 1
        if a_k == 0 :   # Completion check. When a_k == 0 calculations for pi is done
            break
    total = 13591409*a_sum + 545140134*b_sum
    pi = (426880*sqrt(10005*one, one)*one) // total
    return pi

def main() :
    resolution = 5 # Defines how many iterations to take. Logarithmic scale (ie 5 is 10000)
    start = time() # Timestamp for timing
    for log10_digits in range(1,resolution): #Defines how many iterations to take. Logarithmic scale (ie 5 is 10000)
        digits = 10**log10_digits
        one = 10**digits
        pi = pi_chudnovsky(one)
        print("Pi to ", digits," digits precision in ", time()-start," seconds")
        print(pi)

if __name__ == "__main__":
    main()