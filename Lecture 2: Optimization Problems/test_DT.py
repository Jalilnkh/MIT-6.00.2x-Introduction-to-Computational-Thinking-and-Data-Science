import random
random.seed(0)

from decision_tree import decision_tree
from menu import build_menu


def test_decision_tree(items, constraint):
    val, taken = decision_tree(items, constraint)
    print(f"Total value of taken menu is : {val}")
    for item in taken:
        print('  ', item)


if __name__ == "__main__":
    calories = [random.randint(100, 400) for _ in range(10)]
    values = [random.randint(100, 400) for _ in range(10)]
    names = ['آلما','آرمود','نار','اۆزوم','چیلک','شافتالی','آلبالی','قارپیز','بؤیورتکن','اریک']
    max_cost = 1000
    menu = build_menu(names, values, calories)
    test_decision_tree(menu, max_cost)
    

