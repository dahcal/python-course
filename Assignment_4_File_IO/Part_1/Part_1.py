"""
Python 3 program to output a sorted list of text files in the directory fo the script and any subdirectories
"""

import os
from pathlib import Path
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

## Parses a provided text and proived the frequency of words
def getwordfreqs(file_path):

    #file_text = file_path #For texting with set text

#    with open(file_path,encoding="utf8") as f:      # With closes the file automatically https://docs.python.org/3/reference/compound_stmts.html#with
#        file_text = f.read()

    with open(file_path, encoding='utf-8') as f:      # With closes the file automatically https://docs.python.org/3/reference/compound_stmts.html#with
        file_text = f.read()

    file_text_lower = file_text.lower()
    word_list = file_text_lower.split()

    word_freq = []
    del_list = []

#    for i in range(len(word_list)):
#        if word_list[i].isalnum():
#            word_freq.append(word_list.count(i))
#        else:
#            del_list.append(i)
#
#    for i in del_list:
#        del word_list[i]

    
    for i in word_list:
        word_freq.append(word_list.count(i))

#    print("List\n" + str(word_list) + "\n")
#    print("Frequencies\n" + str(word_freq) + "\n")
#    print("Pairs\n" + str((word_list, word_freq)))

    word_freq_zip = zip(word_freq,word_list)
    word_freq_zip_sort = sorted(word_freq_zip, key= lambda t: t[1],reverse=True)
    print(word_freq_zip_sort)

    #freq_zip_sort = sorted(word_freq_zip)
    #for j in range(len(freq_zip_sort)):
    #    print(freq_zip_sort[j],)
    return dict(word_freq_zip)



if __name__ == "__main__":
    data_path = "books"
    file_path = getfilelist(data_path)

    dicts = []
    #for i in file_path:
    #    dicts.append(getwordfreqs(i))

    ## Test with only 1 file
    dicts.append(getwordfreqs(file_path[1]))
    print(dicts)

    #for i in range(10):
    #    print(dicts[i])

    #for w in getcommonwords(dicts):
    #    print(w)


    #wordstring = 'it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness'   
    #getwordfreqs(wordstring)
