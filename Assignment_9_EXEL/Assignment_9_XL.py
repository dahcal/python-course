'''
    Python 3 program that reads an excel file of fertility data and prints the highest and lowest fertility as well as the greatest increase.

    Author: Oscar Calisch
'''

import openpyxl
import Country

FILENAME = 'Fertility.xlsx' # While reading directly from the xlsx file is inline wiht the task, ocnverting to a csv would make it much faster

DEBUG = False   # Debug flag. Tons of spam if enabled
DEBUG_DATA = False # Debug flag. Uses local example data to reduce wait time on file read.


# Example data used for testing. Reading the excel file each time took too long.
exdata = {'Afghanistan': {'Around 1970': 8.21, '..': 7.11, 'Around 2005': 7.52, 'Latest': 5.11}, 'Albania': {'Around 1970': 5.16, 'Around 1985': 3.33, 'Around 1995': 2.86, 'Around 2005': 1.61, 'Latest': 1.33}, 'Algeria': {'Around 1970': 7.86, 'Around 1985': 5.35, 'Around 1995': 4.38, 'Around 2005': 2.38, 'Latest': 2.74}, 'American Samoa': {'Around 1970': 5.83, 'Around 1985': 4.18, 'Around 1995': 3.97, 'Around 2005': 4.1, 'Latest': 3.38}, 'Andorra': {'Around 1995': 1.08, 'Around 2005': 1.27, 'Latest': 1.25}, 'Angola': {'Around 1970': 6.7, 'Around 1985': 7, 'Around 1995': 6.91, 'Around 2005': 5.79, 'Latest': 5.8}, 'Anguilla': {'Around 1985': 2.91, 'Around 1995': 1.84, 'Around 2005': 1.44, 'Latest': 1.54}, 'Antigua and Barbuda': {'Around 1970': 2.68, 'Around 1985': 1.86, 'Around 1995': 2.2, 'Around 2005': 2.36, 'Latest': 2.01}, 'Argentina': {'Around 1970': 3.07, 'Around 1985': 2.96, 'Around 1995': 2.56, 'Around 2005': 2.38, 'Latest': 2.38}, 'Armenia': {'Around 1970': 3.16, 'Around 1985': 2.52, 'Around 1995': 1.63, 'Around 2005': 1.37, 'Latest': 1.56}, 'Aruba': {'Around 1970': 2.53, 'Around 1985': 1.94, 'Around 1995': 2.08, 'Around 2005': 1.74, 'Latest': 1.61}, 'Australia': {'Around 1970': 2.86, 'Around 1985': 1.89, 'Around 1995': 1.82, 'Around 2005': 1.79, 'Latest': 1.88}, 'Austria': {'Around 1970': 2.31, 'Around 1985': 1.48, 'Around 1995': 1.41, 'Around 2005': 1.41, 'Latest': 1.44}, 'Azerbaijan': {'Around 1970': 4.63, 'Around 1985': 2.9, 'Around 1995': 2.19, 'Around 2005': 2.33, 'Latest': 1.93}, 'Bahamas': {'Around 1970': 3.38, 'Around 1985': 2.48, 'Around 1995': 2.47, 'Around 2005': 1.9, 'Latest': 1.89}, 'Bahrain': {'Around 1970': 6.7, 'Around 1985': 4.53, 'Around 1995': 3.01, 'Around 2005': 2.61, 'Latest': 2.06}, 'Bangladesh': {'Around 1970': 6.08, 'Around 1985': 4.61, 'Around 1995': 3.26, 'Around 2005': 3.02, 'Latest': 2.32}, 'Barbados': {'Around 1970': 2.97, 'Around 1985': 1.86, 'Around 1995': 1.74, 'Around 2005': 1.9, 'Latest': 1.83}, 'Belarus': {'Around 1970': 2.36, 'Around 1985': 2.08, 'Around 1995': 1.38, 'Around 2005': 1.2, 'Latest': 1.51}, 'Belgium': {'Around 1970': 2.24, 'Around 1985': 1.55, 'Around 1995': 1.56, 'Around 2005': 1.75, 'Latest': 1.82}, 'Belize': {'Around 1970': 6.25, 'Around 1985': 5.02, 'Around 1995': 4, 'Latest': 3.4}, 'Benin': {'..': 6.93, 'Around 1985': 7.08, 'Around 1995': 5.96, 'Around 2005': 5.74, 'Latest': 4.9}, 'Bermuda': {'Around 1970': 1.86, 'Around 1985': 1.85, 'Around 1995': 1.74, 'Around 2005': 1.81, 'Latest': 1.81}, 'Bhutan': {'Around 1985': 5.9, 'Around 1995': 5.59, 'Around 2005': 4.69, 'Latest': 2.51}, 'Bolivia (Plurinational State of)': {'Around 1970': 6.81, 'Around 1985': 5.04, 'Around 1995': 4.23, 'Around 2005': 3.84, 'Latest': 3.54}, 'Bosnia and Herzegovina': {'Around 1970': 2.65, 'Around 1985': 1.91, 'Around 1995': 1.71, 'Around 2005': 1.2, 'Latest': 1.27}, 'Botswana': {'Around 1970': 6.5, 'Around 1985': 4.54, '..': 4.86, 'Around 2005': 3.27, 'Latest': 3.18}, 'Brazil': {'Around 1970': 5.15, 'Around 1985': 3.37, 'Around 1995': 2.54, 'Around 2005': 2.01, 'Latest': 1.84}, 'British Virgin Islands': {'Around 1970': 3.57, 'Around 1985': 1.92, 'Around 1995': 2.19, 'Around 2005': 1.99, 'Latest': 1.32}, 'Brunei Darussalam': {'Around 1970': 5.84, 'Around 1985': 3.59, 'Around 1995': 2.74, 'Around 2005': 2.27, 'Latest': 1.76}, 'Bulgaria': {'Around 1970': 2.17, 'Around 1985': 1.97, 'Around 1995': 1.23, 'Around 2005': 1.31, 'Latest': 1.49}, 'Burkina Faso': {'..': 6.68, 'Around 1985': 7.18, 'Around 1995': 6.44, 'Around 2005': 5.88, 'Latest': 6}, 'Burundi': {'Around 1970': 6.13, 'Around 1985': 6.95, 'Around 1995': 6.69, 'Around 2005': 5.6, 'Latest': 6.38}, 'Cambodia': {'..': 3.78, 'Around 1995': 5.64, 'Around 2005': 3.4, 'Latest': 3.05}, 'Cameroon': {'..': 6.38, 'Around 1985': 5.82, 'Around 1995': 4.8, 'Around 2005': 4.97, 'Latest': 5.09}, 'Canada': {'Around 1970': 2.26, 'Around 1985': 1.65, 'Around 1995': 1.64, 'Around 2005': 1.55, 'Latest': 1.67}, 'Cape Verde': {'Around 1970': 5.66, 'Around 1985': 7, 'Around 1995': 4.03, 'Around 2005': 3.98, 'Latest': 2.9}, 'Cayman Islands': {'Around 1970': 4.24, 'Around 1985': 1.79, 'Around 1995': 1.66, 'Around 2005': 1.87, 'Latest': 1.89}, 'Central African Republic': {'Around 1970': 5.84, 'Around 1985': 6.07, 'Around 1995': 5.08, 'Latest': 5.15}, 'Chad': {'..': 5.08, 'Around 1995': 6.37, 'Around 2005': 6.34}, 'Chile': {'Around 1970': 3.57, 'Around 1985': 2.33, 'Around 1995': 2.23, 'Around 2005': 1.82, 'Latest': 1.93}, 'China': {'Around 1970': 5.74, 'Around 1985': 2.36, 'Around 1995': 1.86, 'Around 2005': 1.33, 'Latest': 1.47}}

def read_fertility(file_name):
    '''
        Reads the fertility data from the excel and adds it a dictionary for future use

        TAKES :
            string -- file name/path

        RETURNS :
            dict() -- all data from relevant columns
    '''
    wb = openpyxl.load_workbook(file_name, read_only=True)
    sheet = wb['Fertility ']
    rows = sheet.rows
    data = {}
    record = {}
    tmp = {}
    key = 'A0'
    for row in range(3, sheet.max_row+1):       
        for column in "ACF":
            cell_name = "{}{}".format(column, row)
            if column == 'A':
                key = sheet[cell_name].value
            else:
                if column == 'C':
                    key2 = sheet[cell_name].value
                else:
                    record[key2] = sheet[cell_name].value

            if bool(record):
                data.setdefault(key, {}).update(record)
                record = {}
    return data

def find_max(data):
    '''
        Takes in a dictionary in the format { Nation : { Period : Fertility , (...)} }
        and returns the highest fertility on record

        TAKES:
            dict() -- all country data
        RETURNS:
            dict() -- highest fertility country and what period
    '''

    #Definitions
    max_fert = 0
    fertility = 0
    max_period = ""
    max_nation = ""
    return_data = {}

    # Code
    for nation, info in data.items():
        for period in info:
            fertility = info[period]
            try :
                if fertility > max_fert :
                    max_fert = fertility
                    max_period = period
                    max_nation = nation
            except: pass
    return_data = {max_nation : {max_period : max_fert}}
    return return_data

def find_latest_max(data):
    '''
        Takes in a dictionary in the format { Nation : { Period : Fertility , (...)} }
        and returns the highest latest fertility on record

        TAKES:
            dict() -- all country data
        RETURNS:
            dict() -- highest fertility country and what period
    '''

    #Definitions
    max_fert = 0
    fertility = 0
    max_period = ""
    max_nation = ""
    return_data = {}

    # Code
    for nation, info in data.items():
        try:
            if DEBUG :
                print(fertility)

            fertility = info['Latest']
            
        except KeyError: 
            if DEBUG :
                print(nation, "KeyError")
            fertility = 0
            pass

        try :
            if fertility > max_fert :
                max_fert = fertility
                max_period = 'Latest'
                max_nation = nation
                
        except: pass
         
    return_data = {max_nation : {max_period : max_fert}}
    return return_data

def find_min(data):
    '''
        Takes in a dictionary in the format { Nation : { Period : Fertility , (...)} }
        and returns the lowest fertility on record

        TAKES:
            dict() -- all country data
        RETURNS:
            dict() -- lowest fertility country and what period
    '''

    # Definitions
    min_fert = 999
    fertility = 0
    min_period = ""
    min_nation = ""
    return_data = {}

    # Code
    for nation, info in data.items():
        for period in info:
            fertility = info[period]
            try :
                if fertility < min_fert :
                    min_fert = fertility
                    min_period = period
                    min_nation = nation
            except: pass
    return_data = {min_nation : {min_period : min_fert}}
    return return_data

def find_latest_min(data):
    '''
        Takes in a dictionary in the format { Nation : { Period : Fertility , (...)} }
        and returns the lowest latest fertility on record

        TAKES:
            dict() -- all country data
        RETURNS:
            dict() -- lowest fertility country and what period
    '''

    # Definitions
    min_fert = 999
    fertility = 0
    min_period = ""
    min_nation = ""
    return_data = {}

    # Code
    for nation, info in data.items():
        try:
            if DEBUG :
                print(fertility)

            fertility = info['Latest']
            
        except KeyError: 
            if DEBUG :
                print(nation, "KeyError")
            fertility = 999
            pass

        try :
            if fertility < min_fert :
                min_fert = fertility
                min_period = 'Latest'
                min_nation = nation
               
        except: pass

    return_data = {min_nation : {min_period : min_fert}}
    return return_data

def find_increase(data):
    '''
        Takes in a dictionary in the format { Nation : { Period : Fertility , (...)} }
        and returns the greatest increase in fertility

        TAKES:
            dict() -- all country data
        RETURNS:
            list( dict(), float) -- list containing a dict of whihc country and period and a float of the increase in fertility
    '''

    ## Definitions 
    min_fert = 999
    max_fert = 0
    fertility = 0
    dfert = 0
    prev_dfert = 0
    curr_dfert = 0
    maxd_period = ''
    return_data = {}
    return_delta = {}
    curr_dfert = 0.0000
    tmp_period = ''

    # Code
    for nation, info in data.items():               # Go through the data nation by nation
        fertility = 0
        prev_fertility = 0
        dfert = 0
        for period, fert_data in info.items():      # For each nation, go through for each period and look for increases in fertility

            prev_fertility = fertility
            fertility = fert_data

            prev_period = tmp_period
            tmp_period = period
            try :
                if ( prev_fertility != 0 and fertility > prev_fertility ):      # If there is a previous fertility to compare to, compare

                        if DEBUG :
                            print(fertility, '>', prev_fertility, 'fertility')

                        prev_dfert = dfert
                        dfert = fertility - prev_fertility
                        if ( prev_dfert != 0 and dfert > prev_dfert ):          # If the difference is GREATER than the previous delta

                            if DEBUG :
                                print(dfert, '>', prev_dfert, 'dfert')

                            if ( curr_dfert != 0 and dfert > curr_dfert ) :     # If there us a current leader set, compare with the new data
                                curr_dfert = dfert
                                maxd_nation = nation
                                mind_period = prev_period
                                mind_fertility = prev_fertility
                                maxd_period = period
                                maxd_fertility = fertility
                                return_data = {maxd_nation : {mind_period : mind_fertility, maxd_period : maxd_fertility} }
                                return_delta = { 'Fertility Increase' : curr_dfert}

                            elif (curr_dfert == 0) :                            # If no current leader is set, net with the first data
                                curr_dfert = dfert
                                maxd_nation = nation
                                mind_period = prev_period
                                mind_fertility = prev_fertility
                                maxd_period = period
                                maxd_fertility = fertility
                                return_data = {maxd_nation : {mind_period : mind_fertility, maxd_period : maxd_fertility} }
            except: pass
        
    return( return_data, curr_dfert)

if __name__ == "__main__":
    if DEBUG_DATA:
        data = exdata                          # Example data for testing
    else:
        data = read_fertility(FILENAME)         # Format { Nation : { period : fertility}}

    if DEBUG:
        print(data)

    print("")
    print("Maximum fertility recorded: ", find_max(data))
    print("Minimum fertility recorded: ", find_min(data))
    print("")
    print("Maximum latest fertility: ", find_latest_max(data))
    print("Minimum latest fertility: ", find_latest_min(data))
    print("")

    increase = find_increase(data)
    nation = list(increase[0].keys())

    print("Greatest increse in fertility: ", nation[0], increase[1])
    print("The increase occured: ", increase[0][nation[0]])



    

