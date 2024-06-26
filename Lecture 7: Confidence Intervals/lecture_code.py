import random
import pylab
import numpy as np
import math 

def plot_mean(num_dice, num_rolls, num_bins, legend, color, style):
    means = []
    for i in range(num_rolls // num_dice):
        vals = 0
        for j in range(num_dice):
            vals += 5 * random.random()
        means.append(vals / float(num_dice))
    
    pylab.hist(
        means, 
        num_bins,
        color=color,
        label=legend,
        weights=np.ones(len(means)) / len(means),  # Corrected weights
        hatch=style  # Moved out of the weights parameter
    )
    pylab.legend()
    pylab.title('Rolling Continous Dice')
    pylab.xlabel('Value')
    pylab.ylabel('Probabilty')
    pylab.legend()
    return get_mean_std(means)

def get_mean_std(data):
    mean = np.mean(data)
    std = np.std(data)
    return mean, std

def throw_needles(num_needles):
    in_circle = 0
    for _ in range(1, num_needles+1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <=1.0:
            in_circle += 1
    return 4*(in_circle/float(num_needles))

def get_est(num_needles, num_trails):
    estimates = []
    for t in range(num_trails):
        pi_guess = throw_needles(num_needles)
        estimates.append(pi_guess)
    s_dev = std_dev(estimates)
    cur_est = sum(estimates)/len(estimates)
    print(f'Est. = {str(cur_est)} \
        Std. dev. = {str(round(s_dev, 6))}\
        , Needles = {str(num_needles)}')

    return (cur_est, s_dev)

def est_pi(precision, num_trails):
    num_needles = 1000
    s_dev = precision
    while s_dev >= precision/2:
        cur_est, s_dev = get_est(num_needles, num_trails)
        num_needles *= 2
    return cur_est

def std_dev(estimates):
    mean = sum(estimates) / len(estimates)
    variance = sum((x - mean) ** 2 for x in estimates) / len(estimates)
    return math.sqrt(variance)