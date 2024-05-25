def knapsack_memoization(max_cost, wieght_items, value_items, len_wieghts, memo={}):

    if len_wieghts == 0 or max_cost == 0:
        return 0
    
    if memo[len_wieghts][max_cost] != -1:
        return memo[len_wieghts][max_cost]
    
    # If weight of the nth item is more than the capacity, it cannot be included
    if wieght_items[len_wieghts-1] > max_cost:
        memo[len_wieghts][max_cost] = knapsack_memoization(
            max_cost,
            wieght_items,
            value_items,
            len_wieghts-1,
            memo)
    else:
        # Max value obtained by including or excluding the nth item
        include_item = value_items[len_wieghts-1] + knapsack_memoization(
            max_cost-wieght_items[len_wieghts-1], 
            wieght_items,
            value_items, 
            len_wieghts-1, 
            memo)
        exclude_item = knapsack_memoization(
            max_cost-wieght_items[len_wieghts-1],
            wieght_items,
            value_items, 
            len_wieghts-1, 
            memo)
        memo[len_wieghts][max_cost] = max(include_item, exclude_item)

    return memo[len_wieghts][max_cost]


def knapsack(max_cost, weights, values):
    len_wieghts = len(weights)
    # Initialize memoization table with -1
    memo = [[-1 for _ in range(max_cost + 1)] for _ in range(len_wieghts + 1)]
    return knapsack_memoization(max_cost, weights, values, len_wieghts, memo)