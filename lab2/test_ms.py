import unittest
from merge_sort import merge_sort

class MergeSortTestCase(unittest.TestCase):
    def setUp(self):
        self.sorted_case = [1, 2, 3, 4, 5]  
        self.reverse_sorted_case = [5, 4, 3, 2, 1] 
        self.random_case = [4, 2, 5, 1, 3]  
        self.random_case_with_repetition = [5, 2, 9, 2, 1, 8, 3, 1, 4]  

    def test_sorted_case(self):
        merge_sort(self.sorted_case, 0, len(self.sorted_case) - 1)
        self.assertListEqual(self.sorted_case, [1, 2, 3, 4, 5])

    def test_reverse_sorted_case(self):
        merge_sort(self.reverse_sorted_case, 0, len(self.reverse_sorted_case) - 1)
        self.assertListEqual(self.reverse_sorted_case, [1, 2, 3, 4, 5])

    def test_random_case(self):
        merge_sort(self.random_case, 0, len(self.random_case) - 1)
        self.assertListEqual(self.random_case, [1, 2, 3, 4, 5])

    def test_random_case_with_repetition(self):
        merge_sort(self.random_case_with_repetition, 0, len(self.random_case_with_repetition) - 1)
        self.assertListEqual(self.random_case_with_repetition, [1, 1, 2, 2, 3, 4, 5, 8, 9])

if __name__ == "__main__":
    unittest.main()
