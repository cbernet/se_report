import unittest
import pprint 
import operator

from se_report import *


class TestSEReport(unittest.TestCase):
    
    def test_1_parse(self):
        serep = SEReport('data/test_small.xml')
        serep.print_entries(key=operator.itemgetter(1), reverse=True)
        # pprint.pprint(serep.entries)
    
if __name__ == '__main__':
    unittest.main()
