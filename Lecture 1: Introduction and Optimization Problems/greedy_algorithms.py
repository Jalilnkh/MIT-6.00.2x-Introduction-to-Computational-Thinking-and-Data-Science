"""
In this file we have greedy algorithm function
"""

def greedy_algorithm(items, max_cost, key_function):
    copy_items = sorted(items, key=key_function, reverse=True)
    
    result = []
    total_value, total_cost = 0.0, 0.0

    for i in range(len(copy_items)):
        if (total_cost + copy_items[i].get_cost() <= max_cost):
            result.append(copy_items[i])
            total_cost += copy_items[i].get_cost()
            total_value +=copy_items[i].get_value()

    return (result, total_cost)