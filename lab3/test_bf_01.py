import unittest
from bruteforce_01 import *

class TestKnapsackBruteforce(unittest.TestCase):
    def setUp(self):
        #Basic case
        self.weights1 = [10, 20, 30]
        self.values1 = [60, 100, 120]
        self.capacity1 = 50
        
        #Small capacity
        self.weights2 = [5, 10, 15]
        self.values2 = [50, 60, 90]
        self.capacity2 = 8
        
        #All items fit exactly
        self.weights3 = [10, 20, 30]
        self.values3 = [60, 100, 120]
        self.capacity3 = 60
        
        #No items fit
        self.weights4 = [10, 20]
        self.values4 = [60, 100]
        self.capacity4 = 5
        
        #Single item
        self.weights5 = [10]
        self.values5 = [60]
        self.capacity5 = 15

    def test_basic_case(self):
        max_value, items_included = knapsack_bruteforce(self.weights1, self.values1, self.capacity1)
        self.assertGreater(max_value, 0)
        total_weight = sum(w * c for w, c in zip(self.weights1, items_included))
        self.assertLessEqual(total_weight, self.capacity1)

    def test_small_capacity(self):
        max_value, items_included = knapsack_bruteforce(self.weights2, self.values2, self.capacity2)
        self.assertGreater(max_value, 0)
        total_weight = sum(w * c for w, c in zip(self.weights2, items_included))
        self.assertLessEqual(total_weight, self.capacity2)

    def test_all_items_fit(self):
        max_value, items_included = knapsack_bruteforce(self.weights3, self.values3, self.capacity3)
        self.assertGreater(max_value, 0)
        total_weight = sum(w * c for w, c in zip(self.weights3, items_included))
        self.assertLessEqual(total_weight, self.capacity3)
        self.assertEqual(total_weight, self.capacity3)

    def test_no_items_fit(self):
        max_value, items_included = knapsack_bruteforce(self.weights4, self.values4, self.capacity4)
        self.assertEqual(max_value, 0)
        self.assertListEqual(items_included, [0, 0]) 

    def test_single_item(self):
        max_value, items_included = knapsack_bruteforce(self.weights5, self.values5, self.capacity5)
        self.assertEqual(len(items_included), 1)
        self.assertEqual(items_included[0], 1) 
        self.assertEqual(max_value, self.values5[0])

if __name__ == "__main__":
    unittest.main()