"""
    Python 3 program to sort a list fo string by length and lexicograpically

    Author: Oscar Calisch
"""

# DEBUG
DEBUG = False


# Constants
TEST_LIST = ["aaa", "qwer", "ddd", "bbb", "abc", "dcba"]    # Test list of data
INPUT_FILE = "input.txt"                                    # File name in same directory. Assumed a txt with comma separated entries
INPUT_FILE_SEPARATOR = 0                                    # 0 = comma separator , 1 = line separator
SORT_DIRECTION = True                                       # Print direction for sorted data. False is ascending, True is decending. Also affects lexicoghraphical for merge sort


def sort(string_list):
    """
        Python uses a stable sort, meaning that the order is kept if you sort by some other parameter. 
        This is utlized to sort lexicographically first, then by length. 
        Thus the lex sort is kept through through the length sort.
    """
    string_list.sort()
    string_list.sort(key=len, reverse=SORT_DIRECTION)

    return(string_list)

def merge_sort(seq, key=lambda x: x, reverse = False):
    """
        This implementation of merge sort is not stable, meaning the order is not necessarily the same in output and input.
        The sort produces a lexicographical and length based sort at the same time.
    """

    # In the chance the list is of length 1
    if len(seq) == 1:
        return seq
    else:
        # Recursive step. Break the list into chunks of 1
        mid_index = len(seq) // 2
        left  = merge_sort( seq[:mid_index], key )
        right = merge_sort( seq[mid_index:], key )
        
    # Initialize counters at 0
    left_counter, right_counter, master_counter = 0, 0, 0

    # Ensure the counters are correct length
    while left_counter < len(left) and right_counter < len(right):
        if key(left[left_counter]) < key(right[right_counter]):
            seq[master_counter] = left[left_counter]
            left_counter += 1
        else:
            seq[master_counter] = right[right_counter]
            right_counter += 1

        master_counter += 1

    # Handle the remaining items in the remaining_list
    # Either left or right is done already, so only one of these two loops will execute

    while left_counter < len(left):     # Left list is not done, sort left list
        seq[master_counter] = left[left_counter]
        left_counter   += 1
        master_counter += 1

    while right_counter < len(right):   # Right list is not done, sort right list
        seq[master_counter] = right[right_counter]
        right_counter   += 1
        master_counter  += 1
    
    if reverse:                         # Reverse the sorted list. This is why the lexicographical order changes. 
        seq.reverse()
    return seq

if __name__ == "__main__" :

    if DEBUG:
        sorted = sort(TEST_LIST)
        print("Py",sorted)
        sorted = merge_sort(TEST_LIST)
        print("Merge",sorted)

    with open(INPUT_FILE) as file:
        if INPUT_FILE_SEPARATOR == 0:       # Use comma separator
            data = file.read().split(",")
        elif INPUT_FILE_SEPARATOR == 1:     # Use line separator
            data = file.read().splitlines()
        else:
            Exception("Unknown file separator defined")
        print("Pre sort:",)                 # Prints data pre-sort. Printed with a line separated for readability
        print(data)                         
        sorted = sort(data)                 # Print could have been done in a single line, but this is a bit more clear and easier to manipulate further
        print("Py Sorted: ")                # Prints sorted data using pythons "Timsort". Printed with a line separated for readability
        print(sorted)

        mergesorted= merge_sort(data, key = len, reverse = SORT_DIRECTION)    # Note that for merge sort the reverse also affects the lexicographical sort. It's a weakness of my implementation
        print("Merge Sorted:")
        print(mergesorted)

        
    
    
