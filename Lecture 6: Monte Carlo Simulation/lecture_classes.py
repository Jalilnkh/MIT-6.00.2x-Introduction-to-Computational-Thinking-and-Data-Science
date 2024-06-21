import random

class FairRoulette():
    def __init__(self) -> None:
        self.pockets = []
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.pockets_odds = len(self.pockets) - 1
    
    def spin(self):
        self.ball = random.choice(self.pockets)
    
    def bet_pockets(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pockets_odds
        else: return -amt
    
    def __str__(self) -> str:
        return 'Fair Roulette'
    

class EuRoulette(FairRoulette):
    def __init__(self) -> None:
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self) -> str:
        return 'Eu Roulette'

class AmRoulette(EuRoulette):
    def __init__(self) -> None:
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self) -> str:
        return 'USA Rolette'