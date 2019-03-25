"""
    Python 3 program to identify image files from their magic number/magic string and sort them into directories accordingly
   
    Arguments:
        Image files or directories. Unlimited number
    Returns:
        The file type of the arguments
    Raises:
        Error is the input is neither a file or directory
    
    Author: Oscar Calisch
"""

import os
import sys
import shutil
import file_info        # "Homebrew" library separated out as it proved easier for readability and usage (sub-definitions and class invocation). Inspired by the fleep library for file definitions (mainly through a blog post (https://hackernoon.com/determining-file-format-using-python-c4e7b18d4fc4) and reading the source(https://github.com/floyernick/fleep-py))

DEBUG = True            # Debug statement. Set to false to reduce console output

data_path = "images"    # Location to add sorted images


## Directory parser. Adds all found files to the list and returns the list
def get_file_list(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
                file_list.append(os.path.join(root, file))
    file_list = sorted(file_list)
    return(file_list)

## Checks for the magicbyte and prints out what filetype it is
def get_file_type(file_input):
    with open(file_input, "rb") as file:
        info = file_info.get(file.read(8))          # 8 is barely enough to define the files for the assignment. This means it will NOT be futureproof without increasing the bytes read
    print(file_input," is of type ",info.extension)
    return(info.extension)


## Rename the file so the extension matches the magic number
def file_type_rename(file_input):
    with open(file_input, "rb") as file:
        info = file_info.get(file.read(8))         # 8 is barely enough to define the files for the assignment. This means it will NOT be futureproof without increasing the bytes read

    ext = info.extension[0]     # zero index is the image files (in the case of dual identity), hence index 0 is hardcoded for this assignment. There is functionality for testing file type and setting the index accordingly
    pre_tmp, ext_tmp = os.path.splitext(file_input)
    ext_file = ext_tmp[1:]
    ext = str(ext)
    ext_file = str(ext_file)

    if ext == ext_file :
        print ("Extension correct.  File name: ", file_input)
        return(file_input) 
    else:
        pre = os.path.splitext(file_input)[0]
        ext_cln = "".join(ext)
        new_ext = "."+ext_cln
        new_file_name = pre + new_ext
        os.rename(file_input, new_file_name)
        print("Extension error. New file name: ", new_file_name)
        return(new_file_name)
        
## Creates a directory with name dirname in location destpath
def create_dir(dirname, destpath):
    full_path = os.path.join(destpath, dirname)
    try:
        os.mkdir(full_path)
    except FileExistsError:     # If the directory exists do nothing
        pass
    return full_path

def dir_sort(file_input):
    # Takes the extention from the file name and removes the pediod (always first character)
    pre, ext = os.path.splitext(file_input)
    ext_cln = ext[1:]
    
    create_dir(data_path, os.getcwd())

    # Creates a new directory. If it already exists nothing will happen
    move_to = create_dir(ext_cln, data_path)
    file_path = os.path.split(file_input)[0]
    
    if os.path.samefile(file_path, move_to):            # Check if the file is already in the correct directory
        print(file_input, "is already in ", move_to)
    else :                                              # If not, move it there.
        try:                                            # Try to move it
            shutil.move(file_input, move_to)
            print(file_input, "is moved to ", move_to)
        except shutil.Error:                            # Error exception if there already is a file of the same name
            print("File with the same name already exists. Move failed. ", file_input)
            new_name = pre + "(1)" + ext
            input_text = input(("Would you like to call it " , new_name , " instead? (y/n)"))   # If the move failed, ask if user want to rename the file
            input_text.lower()
            if input_text is y:                                                             # If input is "y" then rename file and move
                new_path = os.rename(file_input, new_name)
                shutil.move(new_path, move_to)
                print(file_input, "is moved to ", move_to)
            pass

if __name__ =="__main__" :

    console_input = sys.argv
#    console_input = ["junk", "image"]  # Testing line. Purely so you can use code step-in debugger.

    if len(console_input) > 1  :
        # Remove the .py file from the arguments
        console_input.reverse()
        console_input.pop()

        if DEBUG:                   # If debug flag is set, return the input arguments in original order
            console_input.reverse()
            print("Arguments:", console_input)

        file_list_pub = []          # Define the public/global file list

        for i in console_input :

            # Check if the input is a file or directory
            # If it is a directory, scan through the contents and add them to the file list
            if os.path.isdir(i) :
                tmp_list = get_file_list(i)
                for y in tmp_list :             # Add contents to file list individually to avoid list in list
                    file_list_pub.append(y)
            elif os.path.isfile(i):             # If it is a file, add it directly to the list
                file_list_pub.append(i)
            else :                              # If it is neither a file or directory, throw an error and exit (no handling of this exception in code)
                print("ERROR: Unable to determine if argument is a file or directory")
                print("Exiting")
                input("Press any button...")
                exit()
 
        print("")                   # Prints an empty line for readability  

        #   Goes through the file list and verifies the file type before sorting
        for i in file_list_pub :
            get_file_type(i)        # Check what the file type is. Print the type
            new_name = file_type_rename(i)     # Renames the file if it has the wrong extension
            dir_sort(new_name)             # Sorts the files to directories based on the extension. If a directory does not exist it will create one.
            print("")               # Prints an empty line for readability  

    else :
        print("ERROR: Requires arguments (files or directories)")
