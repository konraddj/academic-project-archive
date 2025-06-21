"""
Update Letter convertions, KDJ
"""
import unittest

import formater

class TestFormatter(unittest.TestCase):
    '''Create a new class for test lower and upper letters'''
    def test_lower(self):
        '''Create function for lower letters'''
        test_text = "JOHN ORAW"
        result = formater.convert_lower(test_text)
        self.assertEqual(result, "john oraw")
    def test_upper(self):
        '''Create function for upper letters'''
        test_text = "John ORaw"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "JOHN ORAW")
if __name__ =="__main":
    unittest.main()
