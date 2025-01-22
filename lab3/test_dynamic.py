import unittest
from dynamic_01 import *

class TestKnapsack01(unittest.TestCase):
    
    def test_basic_case(self):
        weights = [1, 2, 3]
        values = [10, 20, 30]
        capacity = 5
        result = knapsack_01(weights, values, capacity)
        self.assertEqual(result, 50) 
    
    def test_no_items(self):
        weights = []
        values = []
        capacity = 5
        result = knapsack_01(weights, values, capacity)
        self.assertEqual(result, 0) 
    
    def test_single_item_fits(self):
        weights = [3]
        values = [50]
        capacity = 5
        result = knapsack_01(weights, values, capacity)
        self.assertEqual(result, 50) 
    
    def test_single_item_does_not_fit(self):
        weights = [10]
        values = [100]
        capacity = 5
        result = knapsack_01(weights, values, capacity)
        self.assertEqual(result, 0) 
    
    def test_multiple_items_all_fit(self):
        weights = [2, 3, 4]
        values = [30, 40, 50]
        capacity = 9
        result = knapsack_01(weights, values, capacity)
        self.assertEqual(result, 120) 
    
    def test_multiple_items_some_fit(self):
        weights = [3, 4, 5]
        values = [50, 60, 70]
        capacity = 8
        result = knapsack_01(weights, values, capacity)
        self.assertEqual(result, 120) 

if __name__ == "__main__":
    unittest.main()
