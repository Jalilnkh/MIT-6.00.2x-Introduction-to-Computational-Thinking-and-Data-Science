
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