import unittest
from binarysearch import *
class TestSearch (unittest.TestCase):
    def test_element_found_at_first_index(self):
        input_data = [4,5,7,8,10,12]
        result = search(input_data, 4)
        self.assertEqual(result, 0)

    def test_element_found_at_last_index(self):
        input_data = [4,5,7,8,10,12]
        result = search(input_data, 12)
        self.assertEqual(result, 5)

    def test_element_found_at_middle_index(self):
        input_data = [4,5,7,8,10,12]
        result = search(input_data, 7)
        self.assertEqual(result, 2)

    def test_element_not_found(self):
        input_data = [4,5,7,8,10,12]
        result = search(input_data, 6)
        self.assertEqual(result, -1)
    
if __name__ =="__main__":
    unittest.main()

