# NOTE: Change the import below to reflect your filename
from Assignment_8_RLE import RLEString

if __name__ == '__main__':
    tests = ["aaa", "a", "TTTTTeeeesssst", "AAAABBBBCCCCDEFGHIIIIIIJJ", "There are more than 3 non-alphabeticals in this one when we count spaces!", "abcdefghjiklmno", ""]
    
    for t in tests:
        try:
            rle = RLEString(t)
    
            print("Original: %s"%(rle))
            rle.compress()
            compressed = rle.__str__()
            if compressed == t:
                raise Exception("Original string equals compressed!")
                pass
    
            print("Compressed: %s"%(rle))
    
            rle.decompress()
            if not rle.__str__() == t:
                raise Exception("Compression error, expected original after decompress!")
    
            rle.decompress()
            rle.compress()
            rle.compress()
    
        except Exception as e:
            print(e)
            pass