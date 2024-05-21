"""
In this file we have:
1- Food class which has name, value and calories 
2- build menu function
3- greedy algorithm function
"""

class Food:
    def __init__(self, name, value, calories) -> None:
        self.name = name
        self.value = value 
        self.calories = calories
    
    def get_value(self):
        return self.value
    
    def get_cost(self):
        return self.calories
    
    def __str__(self) -> str:
        return self.name + ': <' + str(self.value)\
            + ', ' + str(self.calories) + '>'
    

def build_menu(names, values, calories):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

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