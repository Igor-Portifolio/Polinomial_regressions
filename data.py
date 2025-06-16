import random

# prepare data
def make_data(k):
    x = [100 * random.random() for i in range(k)]  # positions of the points in the plane
    y = [100 * random.random() for i in range(k)]
    return x, y