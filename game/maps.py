import numpy as np

class Map:

    def __init__(self):
        self.levels= []


class Levels:

    def __init__(self):
        dimension = (255, 255)
        self.bg = np.ndarray(dimension, dtype=np.uint8)
        self.entities = []
