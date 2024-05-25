from memoization_knapsack import knapsack

if __name__ == "__main__":
    # Example usage
    cost = 150  # Maximum capacity of knapsack
    weights = [10, 20, 30]  # Weights of items
    values = [60, 100, 120]  # Values of items

    max_value = knapsack(cost, weights, values)
    print("Maximum value in Knapsack:", max_value)