import random
from field import Field
from drunk import Drunk, UsualDrunk
from location import Location

def single_walk(f_class, d_class, num_steps):
    start = f_class.get_loc(d_class)
    for s in range(num_steps):
        f_class.move_drunk(d_class)
    return start.dist_from(f_class.get_loc(d_class))

def multi_walk(num_steps, num_trails, d_class):
    homer = d_class('Homer')
    origin = Location(0,0)
    distances = []
    for t in range(num_trails):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(single_walk(f, homer, num_steps), 1))  # Use num_steps here

    return distances

def drunk_test(walk_lengths, num_trails, d_class):
    for num_steps in walk_lengths:
        distances = multi_walk(num_steps, num_trails, d_class)
        print(f"{d_class.__name__} Random walk of {num_steps} steps")
        print(f"Mean = {round(sum(distances)/len(distances), 4)}")
        print(f"Max = {max(distances)} Min = {min(distances)}")

if __name__ == "__main__":
    random.seed(0)
    drunk_test((10, 100, 1000, 1000), 100, UsualDrunk)
