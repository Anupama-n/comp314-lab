import unittest
from greedy_fractional import *

class TestFractionalKnapsack(unittest.TestCase):
    
    def setUp(self):
        #Basic case
        self.items1 = [Item(60, 10), Item(100, 20), Item(120, 30)]
        self.capacity1 = 50
        
        #All items too large for the capacity
        self.items2 = [Item(60, 10), Item(100, 50), Item(120, 60)]
        self.capacity2 = 10
        
        #Exact fit with whole items
        self.items3 = [Item(60, 10), Item(100, 20), Item(120, 30)]
        self.capacity3 = 60
        
        #Empty
        self.items4 = [Item(60, 10), Item(100, 20)]
        self.capacity4 = 0
        
        #Single item fits perfectly
        self.items5 = [Item(60, 10)]
        self.capacity5 = 10

    def test_basic_case(self):
        max_value = fractional_knapsack(self.capacity1, self.items1)
        self.assertEqual(max_value, 240.0)

    def test_all_items_too_large(self):
        max_value = fractional_knapsack(self.capacity2, self.items2)
        self.assertEqual(max_value, 60.0)

    def test_exact_fit_with_whole_items(self):
        max_value = fractional_knapsack(self.capacity3, self.items3)
        self.assertEqual(max_value, 280.0)

    def test_empty_knapsack(self):
        max_value = fractional_knapsack(self.capacity4, self.items4)
        self.assertEqual(max_value, 0.0)

    def test_single_item_fits_perfectly(self):
        max_value = fractional_knapsack(self.capacity5, self.items5)
        self.assertEqual(max_value, 60.0)

if __name__ == "__main__":
    unittest.main()
