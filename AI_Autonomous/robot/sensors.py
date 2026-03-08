import random

def noisy_distance(true_value):

    noise = random.uniform(-0.5,0.5)

    return true_value + noise