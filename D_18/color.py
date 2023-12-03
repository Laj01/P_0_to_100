import random

def random_color():
    hue = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return hue