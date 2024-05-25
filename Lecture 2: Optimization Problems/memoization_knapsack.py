def knapsack_memoization(cost, wieght_items, value_items, num_items, memo={}):

    if num_items == 0 or cost == 0:
        return 0
    
    if memo[num_items][cost] != -1:
        return memo[num_items][cost]
    
    # If weight of the nth item is more than the capacity, it cannot be included
    if wieght_items[num_items-1] > cost:
        memo[num_items][cost] = knapsack_memoization(
            cost,
            wieght_items,
            value_items,
            num_items-1,
            memo)
    else:
        # Max value obtained by including or excluding the nth item
        include_item = value_items[num_items-1] + knapsack_memoization(
            cost-wieght_items[num_items-1], 
            wieght_items,
            value_items, 
            num_items-1, 
            memo)
        exclude_item = knapsack_memoization(
            cost-wieght_items[num_items-1],
            wieght_items,
            value_items, 
            num_items-1, 
            memo)
        memo[num_items][cost] = max(include_item, exclude_item)

    return memo[num_items][cost]


def knapsack(max_cost, weights, values):
    num_items = len(weights)
    # Initialize memoization table with -1
    memo = [[-1 for _ in range(max_cost + 1)] for _ in range(num_items + 1)]
    return knapsack_memoization(max_cost, weights, values, num_items, memo)