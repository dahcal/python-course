'''
    Python 3 program to unit test Assignment 8 Run-Length Encoding
    Author: Oscar Calisch
'''
import unittest
import sys

# Uncomment below for testing only, comment out before upload
from Assignment_8_RLE import RLEString

succeed_tests = ["aaa", "a", "TTTTTeeeesssst", "AAAABBBBCCCCDEFGHIIIIIIJJ", "abcdefghjiklmno"]
fail_tests= ["There are more than 3 non-alphabeticals in this one when we count spaces!", ""]


class Assignment8Tests(unittest.TestCase):

    def test_compress(self):
        ''' 
            Test if the compress function compresses properly
        '''
        for test in succeed_tests:
            rle = RLEString(test)
            rle.compress()
            result = rle.__str__()
            self.assertNotEqual( result, test )

        for test in fail_tests:
            with self.assertRaises(Exception):
                rle = RLEString(test)
                rle.compress()
                result = rle.__str__()
                self.assertNotEqual( result, test )

    def test_decompress(self):
        ''' 
            Test if the decompress function decompresses properly
        '''
        for test in succeed_tests:
            rle = RLEString(test)
            rle.compress()
            rle.decompress()
            result = rle.__str__()
            self.assertEqual( result, test )

    def test_doubleCompress(self):
        ''' 
            Test if the compress function handles double-compress
        '''
        for test in succeed_tests:
            with self.assertRaises(Exception):
                rle = RLEString(test)
                rle.compress()
                rle.compress()

    def test_doubleDecompress(self):
        ''' 
            Test if the compress function handles double-decompress
        '''
        for test in succeed_tests:
            with self.assertRaises(Exception):
                rle = RLEString(test)
                rle.compress()
                rle.decompress()
                rle.decompress()

    def test_isCompressed(self):
        ''' 
            Test if the compress function updates iscompressed() properly
        '''
        for test in succeed_tests:
            rle = RLEString(test)
            rle.compress()
            result = rle.iscompressed()
            self.assertTrue( result )

    def test_isDeompressed(self):
        ''' 
            Test if the compress function updates iscompressed() properly
        '''
        for test in succeed_tests:
            rle = RLEString(test)
            rle.compress()
            rle.decompress()
            result = rle.iscompressed()
            self.assertFalse( result )



if __name__ == '__main__':

    # Start the unit test
    unittest.main(verbosity=2)