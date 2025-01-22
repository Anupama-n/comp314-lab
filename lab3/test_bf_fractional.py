import unittest
from bruteforce_fractional import *

class FractionalKnapsackTestCase(unittest.TestCase):
    def setUp(self):
        # Test case 1: Basic case
        self.weights1 = [10, 20, 30]
        self.values1 = [60, 100, 120]
        self.capacity1 = 50
        
        # Test case 2: Small capacity
        self.weights2 = [5, 10, 15]
        self.values2 = [50, 60, 90]
        self.capacity2 = 8
        
        # Test case 3: Large values
        self.weights3 = [2, 3, 4, 5]
        self.values3 = [100, 200, 300, 400]
        self.capacity3 = 10
        
        # Test case 4: Empty knapsack
        self.weights4 = [10, 20]
        self.values4 = [60, 100]
        self.capacity4 = 0
        
        # Test case 5: Single item
        self.weights5 = [10]
        self.values5 = [60]
        self.capacity5 = 15

    def test_basic_case(self):
        max_value, fractions = fractional_knapsack_bruteforce(self.weights1, self.values1, self.capacity1)
        self.assertGreater(max_value, 0)
        self.assertEqual(len(fractions), len(self.weights1))
        # Check if total weight doesn't exceed capacity
        total_weight = sum(w * f for w, f in zip(self.weights1, fractions))
        self.assertLessEqual(total_weight, self.capacity1)

    def test_small_capacity(self):
        max_value, fractions = fractional_knapsack_bruteforce(self.weights2, self.values2, self.capacity2)
        self.assertGreater(max_value, 0)
        total_weight = sum(w * f for w, f in zip(self.weights2, fractions))
        self.assertLessEqual(total_weight, self.capacity2)
        # Check if fractions are between 0 and 1
        for fraction in fractions:
            self.assertGreaterEqual(fraction, 0)
            self.assertLessEqual(fraction, 1)

    def test_large_values(self):
        max_value, fractions = fractional_knapsack_bruteforce(self.weights3, self.values3, self.capacity3)
        self.assertGreater(max_value, 0)
        total_weight = sum(w * f for w, f in zip(self.weights3, fractions))
        self.assertLessEqual(total_weight, self.capacity3)
        # Verify that high value-to-weight ratio items are preferred
        value_density = [v/w for v, w in zip(self.values3, self.weights3)]
        max_density_index = value_density.index(max(value_density))
        self.assertGreater(fractions[max_density_index], 0)

    def test_zero_capacity(self):
        max_value, fractions = fractional_knapsack_bruteforce(self.weights4, self.values4, self.capacity4)
        self.assertEqual(max_value, 0)
        # All fractions should be 0 when capacity is 0
        self.assertListEqual(fractions, [0] * len(self.weights4))

    def test_single_item(self):
        max_value, fractions = fractional_knapsack_bruteforce(self.weights5, self.values5, self.capacity5)
        self.assertEqual(len(fractions), 1)
        # Should take entire item since capacity > weight
        self.assertEqual(fractions[0], 1.0)
        self.assertEqual(max_value, self.values5[0])

if __name__ == "__main__":
    unittest.main()