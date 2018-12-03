import pygame as pg


class Entity:
    def __init__(self, location, z_level):
        self.stats = {
            "sight": 1,
            "speed": 0,
            "hp": 1,
            "mp": 0,
            "armour": 0,
            "dodge": 0,
            "agility": 0,
            "strength": 0,
            "crit": 0,
            "hpregen": 0,
            "mpregen": 0,
        }
        self.sprite = pg.Surface()
