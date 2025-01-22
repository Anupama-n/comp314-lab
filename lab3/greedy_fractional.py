class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0.0 
    total_weight = 0 
    
    for item in items:
        if total_weight + item.weight <= capacity:
            total_value += item.value
            total_weight += item.weight
        else:
            remaining_capacity = capacity - total_weight
            total_value += item.value * (remaining_capacity / item.weight)
            break     
    return total_value


