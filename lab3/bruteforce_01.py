from itertools import product

def knapsack_bruteforce(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = [0] * n
    
    for comb in product([0, 1], repeat=n):
        total_weight = sum(w * c for w, c in zip(weights, comb))
        total_value = sum(v * c for v, c in zip(values, comb))
    
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = list(comb)
    
    return max_value, best_combination


