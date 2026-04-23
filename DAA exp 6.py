def fractional_knapsack(capacity, items):
    
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    
    for value, weight in items:
        if capacity == 0:
            break
        
       
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
       
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0
    
    return total_value


items = [(60, 10), (100, 20), (120, 30)]  
capacity = 50

max_value = fractional_knapsack(capacity, items)
print("Maximum value:", max_value)