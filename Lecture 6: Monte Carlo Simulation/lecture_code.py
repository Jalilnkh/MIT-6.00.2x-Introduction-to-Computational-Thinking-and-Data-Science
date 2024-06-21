from lecture_classes import FairRoulette, EuRoulette, AmRoulette
import random
import math 

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


def find_pocket_return(game, num_trials, num_spins, print_results=True):
    results = []
    for t in range(num_trials):
        trial_return = 0
        for s in range(num_spins):
            game.spin()
            trial_return += game.bet_pockets(random.choice(game.pockets), 1)
        results.append(trial_return / num_spins)
    return results

def get_mean_std(X):
    mean = sum(X) / len(X)
    variance = sum([(x - mean) ** 2 for x in X]) / len(X)
    std = math.sqrt(variance)
    return mean, std

if __name__ == "__main__":
    game = FairRoulette()
    for num_spins in (100, 1000000):
        for i in range(3):
            play_roulette_game(game, num_spins, 2, 10, True)

    print("Let's Apply Empirical Rule ...!")
    result_dict = {}
    games = (FairRoulette, EuRoulette, AmRoulette)
    for G in games:
        result_dict[G().__str__()] = []
    num_trials = 100
    for num_spins in (100, 1000, 10000):

        print(f'\nSimulate betting a pocket for {num_trials}\
            trails of {num_spins} spins each')
        for G in games:
            pocket_returns = find_pocket_return(G(), num_trials, num_spins, False)
            mean, std = get_mean_std(pocket_returns)
            result_dict[G().__str__()].append((num_spins,
                100*mean,
                100*std))
            print(f'Exp. return for {G()} = \
                {str(round(100*mean, 3))} % +/- {str(round(100*1.96*std, 3))}\
                % with 95% confidence')
