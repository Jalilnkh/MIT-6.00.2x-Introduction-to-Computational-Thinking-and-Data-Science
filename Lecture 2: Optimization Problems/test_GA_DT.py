import random
import sys
sys.path.append('../Lecture 1: Introduction and Optimization Problems/')

from greedy_algorithms import greedy_algorithm
from decision_tree import decision_tree
from menu import Food, build_menu

# Set random seed for reproducibility
random.seed(0)

def test_greedy(items, constraint, key_function):
    taken, val = greedy_algorithm(items, constraint, key_function)
    print("Greedy Algorithm Output:")
    print(f"Total value of taken menu is : {val}")
    for item in taken:
        print('  ', item)

def test_decision_tree(items, constraint):
    val, taken = decision_tree(items, constraint)
    print("Decision Tree Output:")
    print(f"Total value of taken menu is : {val}")
    for item in taken:
        print('  ', item)

if __name__ == "__main__":
    # Generate random calories and values for the menu items
    calories = [random.randint(100, 400) for _ in range(10)]
    values = [random.randint(100, 400) for _ in range(10)]
    
    # Names of the food items
    names = ['آلما', 'آرمود', 'نار', 'اۆزوم', 'چیلک', 'شافتالی', 'آلبالی', 'قارپیز', 'بؤیورتکن', 'اریک']
    
    # Maximum cost constraint
    max_cost = 1000
    
    # Build the menu with the given names, values, and calories
    menu = build_menu(names, values, calories)
    
    # Test the greedy algorithm
    test_greedy(menu, max_cost, Food.get_value)

    # Test the decision tree algorithm
    test_decision_tree(menu, max_cost)
