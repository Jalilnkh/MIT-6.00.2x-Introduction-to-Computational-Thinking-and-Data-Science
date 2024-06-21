from lecture_classes import FairRoulette

def play_roulette_game(game, num_spins, pocket, bet, to_print):
    tot_pocket = 0
    for i in range(num_spins):
        game.spin()
        tot_pocket += game.bet_pockets(pocket, bet)
    if to_print:
        print(f"{num_spins} spins of {game}")
        print(f"Expected return betting {pocket} = \
            {str(100*tot_pocket/num_spins)} %\n")
    return (tot_pocket/num_spins)


if __name__ == "__main__":
    game = FairRoulette()
    for num_spins in (100, 1000000):
        for i in range(3):
            play_roulette_game(game, num_spins, 2, 10, True)