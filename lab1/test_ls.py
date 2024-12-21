import unittest
from linearsearch import search
class TestSearch (unittest.TestCase):
    def test_element_found_at_first_index(self):
        input_data = [4,7,5,8,10,2]
        result = search(input_data, 6, 4)
        self.assertEqual(result, 0)

    def test_element_found_at_last_index(self):
        input_data = [4,7,5,8,10,2]
        result = search(input_data, 6, 2)
        self.assertEqual(result, 5)

    def test_element_found_at_middle_index(self):
        input_data = [4,7,5,8,10,2]
        result = search(input_data, 6, 8)
        self.assertEqual(result, 3)

    def test_element_not_found(self):
        input_data = [4,7,5,8,10,2]
        result = search(input_data, 6, 12)
        self.assertEqual(result, -1)
    
if __name__ =="__main__":
    unittest.main()