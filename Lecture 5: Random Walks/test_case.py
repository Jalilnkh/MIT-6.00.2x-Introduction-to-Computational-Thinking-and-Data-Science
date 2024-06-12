from field import Field
from drunk import Drunk

def single_walk(f: Field, d: Drunk, num_steps):
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))

def multi_walk(f: Field, d: Drunk, num_steps):
    
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))