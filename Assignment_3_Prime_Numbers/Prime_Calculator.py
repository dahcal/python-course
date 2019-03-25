"""
Python3 program to calculate prime numbers using Sieve of Eratosthenes
Written by Oscar Calisch
"""

from time import time
#Implementation of Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]      # Create a list containing all numbers from 1 to n+1 (as it is 0-indexed)
    p = 2                                   # p starts at 2 as it is the first prime

    while (p*p <= n):                       # Prime sieve function
        if prime[p]:
            for x in range(p*2, n+1, p):    # All number that are a a multiple of p are nolonger considered candidates  
                prime[x] = False            # Set all values in domain to false
        p += 1                              # Increment p by 1
 
    for x in range(2, n):                   # Print out all froun prime in line
        if prime[x]:
            print(x)

def main() :
    num = 7920                              # Prime number 1000 (7919) +1
    start = time()                          # Timestamp for timing
    sieve_of_eratosthenes(num)              # Prime finder
    print("Time :", time()-start)           # Print the time for the calculation (ie excluding time to print to console as that is not script dependend)

                    
    
if __name__ == "__main__":
    main()