import random
import pylab
import numpy as np

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