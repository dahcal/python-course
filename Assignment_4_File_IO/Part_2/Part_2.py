"""
Python 3 program to output a sortet list of text files in the directory fo the script and any subdirectories
"""

import os
import string
from collections import Counter

## Parses the directory provided and returns all text files in directories
## Error from earlier runs identified: not sorting but incorrect joining of output path
def getfilelist(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_list.append(os.path.join(root, file))
    file_list = sorted(file_list)
    return(file_list)

def getwordfreqs(file_path):
    with open(file_path, encoding="utf-8",errors="surrogateescape") as f:      # With closes the file automatically https://docs.python.org/3/reference/compound_stmts.html#with
        file_text = f.read().lower()
        wordcount = Counter(file_text.translate(str.maketrans('','',string.punctuation)).split())
    return wordcount

def getcommonwords(dicts):

    entry_list = []
    temp_list = []
    dictionaries_counter = 0
    for counter in dicts:
        dictionaries_counter += 1
        temp_list = sorted(counter, key=counter.get, reverse=True)      # Generate a sorted list in decentding order from the dictionary values
        del temp_list[10:]                                              # Delete excess values above index 10 (we only want top 10)
        print(temp_list)                                                # Print for debug
        #entry_list.append(temp_list)
        entry_list = entry_list + temp_list
    print(sorted(entry_list))

    duplicates = set([x for x in entry_list if entry_list.count(x) >= dictionaries_counter])
    common_words = duplicates
    return common_words

if __name__ == "__main__":
    data_path = "books"
    file_path = getfilelist(data_path)

    dicts = []
    for i in file_path:
        dicts.append(getwordfreqs(i))

    ## Test with only 1 file
    #dicts.append(getwordfreqs(file_path[1]))
    #print(dicts)

    #Test with limited file numer
    #for i in range(3):
    #   dicts.append(getwordfreqs(file_path[i]))
    #print(dicts)
    print(getcommonwords(dicts))
## Test data
    words1 = {
        'big': 5,    
        'small': 5,  
        'tiny': 5,   
        'little': 3, 
        'huge': 3,   
        'normal': 1 
        }
    
    words2 = {
        'small': 7,
        'little': 5,
        'tiny': 4,  
        'big': 1,   
        'normal': 1,
        'huge': 1  
        }
    
    words3 = {
        'small': 10,
        'big': 8,
        'tiny': 9,
        'little': 7,
        'huge': 7,
        'normal': 1
        }

    #print(getcommonwords(words1, words2, words3))