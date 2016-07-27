import unittest
import os

class Travistest(unittest.TestCase):

    i = 2
    if i > 1:
        print "Hello beautiful!"
    else:
        print "no"
            


if __name__ == '__main__':
    unittest.main()
