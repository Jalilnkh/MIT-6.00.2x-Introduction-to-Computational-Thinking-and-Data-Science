import random 
random.seed(0)
from greedy_algorithm import Food, build_menu, greedy_algorithm

def test_greedy(items, constraint, key_function):
    taken, val = greedy_algorithm(items, constraint, key_function)
    print(f"Total value of taken menu is : {val}")
    for item in taken:
        print('  ', item)


if __name__ == "__main__":
    calories = [random.randint(100, 400) for _ in range(10)]
    values = [random.randint(100, 400) for _ in range(10)]
    names = ['آلما','آرمود','نار','اۆزوم','چیلک','شافتالی','آلبالی','قارپیز','بؤیورتکن','اریک']
    max_cost = 1000
    menu = build_menu(names, values, calories)
    test_greedy(menu, max_cost, Food.get_value)
    

