from . import quad_tree
import random
import numpy as np
import pygame as pg

# Spawn cells are marked with red being = 100 exactly
# Green is the amount of loot that spawns
# Blue is the amount of enemies that spawn
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

type_names = {
    "loot": 0,
    "enemy": 1,
    "friendly": 2,
}


class Map:
    def __init__(self, game):
        self.levels=[]


class Levels:
    def __init__(self, surf: pg.Surface):
        # Turns an image into a level. Lots of stuff needs to be done!
        # Note, unlike standard convention, These arrays are indexed x then y, not that it matters.
        rect = surf.get_rect()
        array_data = pg.surfarray.array3d(surf)
        self.data = np.zeros(rect.size, dtype=np.uint8)
        self.entities = quad_tree.QuadTree(rect)
        self.image_data = {}

        for key in image_to_key_mappings.keys():
            self.data |= (image_to_key_mappings[key] == array_data[:, :, :])*key_to_data_id_mappings[key]

        special_cells = np.argwhere(array_data[:, :, 0] == 50 or array_data[:, :, 0] == 150)
        self.special_cells_data = np.zeros((special_cells.size[0], 5))
        # Special cells data is stored x, y, loot_prob, enemy_prob, friendly_prob

        self.special_cells_data[:, :2] = special_cells

        for i in range(self.special_cells_data.size[0]):
            x, y = self.special_cells_data[i, :2]
            self.special_cells_data[i, 2] = array_data[x, y, 1]  # Green

            if array_data[x, y, 0] == 50:  # Enemy
                self.special_cells_data[i, 3] = array_data[x, y, 2]  # Blue
            elif array_data[x, y, 0] == 50:  # Friendly
                self.special_cells_data[i, 4] = array_data[x, y, 2]  # Also Blue

        # Here, we transform the sum to cumulative sum.
        self.special_cells_data[:, 2:] = np.cumsum(self.special_cells_data[2:], axis=0)
        self.cum_sums = self.special_cells_data[-1, 2:]

    def return_random_location(self, of_type="loot"):
        # Returns an x,y coordinate, weighted as according to the constructor.
        if of_type not in type_names:
            return False
        if self.cum_sums[type_names[of_type]] == 0:
            return None
        choice = random.randrange(self.cum_sums[type_names[of_type]])
        i = 0
        for s in self.special_cells_data[:, type_names[of_type] + 2]:
            if s > choice:
                break
            else:
                i += 1
        return tuple(self.special_cells_data[i, :2])
