def fractional_knapsack_bruteforce(weights, values, capacity):
    """
    Solve the fractional knapsack problem using brute force method.
    
    Args:
    weights (list): List of weights of items
    values (list): List of values of items
    capacity (float): Maximum capacity of knapsack
    
    Returns:
    tuple: (maximum value possible, list of fractions to take of each item)
    """
    n = len(weights)
    max_value = 0
    best_fractions = [0] * n
    
    def calculate_total(fracs):
        total_weight = sum(w * f for w, f in zip(weights, fracs))
        total_value = sum(v * f for v, f in zip(values, fracs))
        return total_weight, total_value
    
    def generate_combinations(current, index):
        nonlocal max_value, best_fractions
        
        if index == n:
            total_weight, total_value = calculate_total(current)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_fractions = current.copy()
            return
        
        for frac in range(11):
            current[index] = frac / 10
            generate_combinations(current, index + 1)
    
    generate_combinations([0] * n, 0)
    return max_value, best_fractions