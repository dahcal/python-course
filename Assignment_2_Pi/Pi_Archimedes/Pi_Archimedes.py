"""
Python3 program to calculate pi to 100 places using Archimedes method
"""

from decimal import Decimal, getcontext
from time import time

def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI
    """
    polygon_edge_length_squared = Decimal(2)    # Decimal for precision
    polygon_sides = 2
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * (1 - polygon_edge_length_squared / 4).sqrt() 
        polygon_sides *= 2
    return polygon_sides * polygon_edge_length_squared.sqrt()

def main():
    """
    Try the series
    """
    # Pi to 1000 places for reference
    Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
    places = 100
    old_result = None
    start = time() # Timestamp for timing 
    for n in range(10*places):
        # Do calculations with double precision
        getcontext().prec = 2*places # Sets precision to 2*places. This is to reduce loss due to rounding
        result = pi_archimedes(n)
        # Print the result with single precision
        getcontext().prec = places
        result = +result           # Do the rounding on result from 2*places to 1*places (ie the number we want)
        error = result - Decimal(Pi) # Simple error calculation
        #print("Result: ", result)
        #print("Error: ", Decimal(error))
        if result == old_result:    # If the numbers we get are the same, break. This is as close as we'll get
            break
        old_result = result
    print("Result: ", result)
    print("Error: ", Decimal(error))
    print("Time: ", time()-start)

if __name__ == "__main__":
    main()
