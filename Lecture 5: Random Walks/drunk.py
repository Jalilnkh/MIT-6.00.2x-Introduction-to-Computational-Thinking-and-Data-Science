import random

class Drunk():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        if self != None:
            return self.name
        return 'Anonymous'
    
class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [
            (0,1), 
            (0,-1), 
            (1,0),
            (-1,0)]
        return random.choice(step_choices)

class MasochistDrunk(Drunk):
    def take_step(self):
        step_choices = [
            (0.0,1.1), 
            (0.0,-0.9), 
            (1.0,0.0),
            (-1.0,0.0)]
        return random.choice(step_choices)
