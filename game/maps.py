from . import quad_tree
import numpy as np
import pygame as pg


image_to_key_mappings = {
    "walls": np.array([0, 0, 0], dtype=np.uint8),
    "air": np.array([255, 255, 255], dtype=np.uint8),
    "up_stairs": np.array([255, 0, 0], dtype=np.uint8),
    "down_stairs": np.array([0, 0, 255], dtype=np.uint8),
}
key_to_data_id_mappings = {
    "air": np.array([0], dtype=np.uint8),
    "wall": np.array([1], dtype=np.uint8),
    "up_stairs": np.array([2], dtype=np.uint8),
    "down_stairs": np.array([3], dtype=np.uint8),
}


class Map:
    def __init__(self, game):
        self.levels=[]


class Levels:
    def __init__(self, surf: pg.Surface):
        # Turns an image into a level. Lots of stuff needs to be done!
        rect = surf.get_rect()
        array_data = pg.surfarray.array3d(surf)
        self.data = np.ndarray(array_data.shape, dtype=np.uint8)

        for key, value in image_to_key_mappings:
            self.data |= (image_to_key_mappings[key] == array_data[:, :, :])
        self.entities = quad_tree.QuadTree(rect)
        self.image_data = {}


