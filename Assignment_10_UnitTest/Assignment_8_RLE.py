from itertools import  groupby

class RLEString:
    """
    Compresses and decompresses text input
    Takes:
        type_ (string) -> string
    Returns:
        (<class 'RLEString'>) -> Class instance
    """

    def __init__(self, intstring_,):
        self.compression_state = False
        self.intstring = intstring_
        self.intlist = []

        if not isinstance(self.intstring, str):                 # Checks if the input is a string
            raise TypeError("Object type myst be string")
        if not self.intstring.isalpha():                        # Checks if the input string is letters only
            raise TypeError("Object must be alphabetical characters only")

    def compress(self):
        """ Compresses the input string """
        obj = self.intstring                                    # Not strictly neccesary, but allows for easier testing and debugging
        lst = []                                                # Instaciates an empty list

        if self.compression_state:                              # Checks the compression state flag
            raise Exception("Already compressed")
        
        lst = [(len(list(g)), k) for k,g in groupby(obj)]       # Convets the string into a tuple of pairs
        self.compression_state = True                   
        self.intlist = lst
        return lst


    def decompress(self):
        """ Decompresses the input string """
        if not self.compression_state:                          # Checks the compression state flag
            raise Exception("Already decompressed")

        obj = self.intlist                                      # Not strictly neccesary, but allows for easier testing and debugging
        self.intstring = ''.join(c * n for n,c in obj)          # Formulaic way to multiply the components of the tuples (number and letter) and joining them to a string
        self.compression_state = False
        return self.intstring

    def iscompressed(self):
        """ Checks if the input string is compressed """
        return self.compression_state

    def __str__(self):
        """ Returns a printable version of the current compression state"""
        obj = self.intlist
        if self.compression_state:                              # If its currently compressed convert it to a string
            data = [[str(x) for x in tup] for tup in obj]       # Converts the tuple of numbers and strings to pure strings
            output = "".join(''.join(c+n for c,n in data))      # Returns a printable version
        else:
            output = self.intstring                             # If it's decompressed, return the internal string
        return output