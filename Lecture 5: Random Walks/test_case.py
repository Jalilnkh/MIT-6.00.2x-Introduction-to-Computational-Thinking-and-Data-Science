from field import Field
from drunk import Drunk
from location import Location


def single_walk(f: Field, d: Drunk, num_steps):
    
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def multi_walk(num_steps, num_trails,d: Drunk):
    homer = d()
    origin = Location(0,0)
    distances = []
    for t in range(num_trails):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(single_walk(f,homer,num_trails), 1))

    
    return distances

