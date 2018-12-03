import pygame as pg
import json

default_texture = pg.image.load("./assets/images/missing_texture.png").convert()


class Entity:
    freeid = 0

    def __init__(self, location, z_level):
        self.uuid = Entity.freeid
        Entity.freeid += 1
        self.name = "GenericEntity"
        self.flavourtext = None
        self.icon = default_texture.copy()
        self.x, self.y = location
        self.z_level = z_level

    # Distance between two entities
    def distance(self, other):
        if self.z_level != other.z_level:
            return 10000

        dx = (self.x - other.x)
        dy = (self.y - other.y)
        return (dx*dx + dy*dy)**(1/2)

    def basic_move(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_in_range_1(self, other):
        if self.z_level == other.z_level:
            if abs(self.x - other.x) <= 1:
                if abs(self.y - other.y) <= 1:
                    return True
        else:
            return False


class Item(Entity):
    def __init__(self, location, z_level, icon):
        super().__init__(location, z_level)
        self.name = "GenericItem"
        self.icon = icon
        self.stats = {}


class Consumable(Item):
    def __init__(self, location, z_level, icon):
        super().__init__(location, z_level, icon)
        self.charges = 0

    def consume(self):
        if self.charges > 0:
            self.charges -= 1
            return self.stats
        else:
            return False


class Equipment(Item):
    def ___init__(self, location, z_level, icon):
        super().__init__(location, z_level, icon)

        # The files are flexible, but in this case equip slots must be one of
        # head, hand, body, foot
        self.equipslots = []


class Mob(Entity):
    def __init__(self, location, z_level, icon):
        super().__init__(location, z_level)
        self.name = "GenericMob"
        self.effects = []
        self.icon = icon
        self.tag = "enemy"
        self.stats = {
            "sight": 1,
            "speed": 0,
            "range": 0,
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

    def real_stat(self, stat):
        base_value = self.stats[stat]
        for effect, strength, duration in self.effects:
            if effect == stat:
                base_value += strength
        return base_value

    def apply_effect(self, effect, strength, duration):
        self.effects.append((effect, strength, duration))

    def tick_effects(self):
        new_effects = []
        for effect, strength, duration in self.effects:
            if duration > 1:
                new_effects.append((effect, strength, duration-1))


class Player(Mob):
    def __int__(self, location, z_level, icon):
        super().__init__(location, z_level, icon)
        self.inventory = []
        self.tag = "friendly"
        self.equipment = {
            "head": None,
            "l_hand": None,
            "r_hand": None,
            "body": None,
            "l_foot": None,
            "r_foot": None,
        }

        self.stats.update({
            "sight": 30,
            "speed": 2,
            "range": 1,
            "hp": 20,
            "mp": 10,
            "armour": 0,
        })

    def equip(self, item, slot):
        if slot in ["l_hand", "l_foot"]:
            check = "hand"
        elif slot in ["l_foot", "r_foot"]:
            check = "foot"
        else:
            check = slot
        if check in item.equipslots:
            self.equipment[slot] = item

    def real_stat(self, stat):
        base_value = super().real_stat(stat)

        for equip in self.equipment.values():
            for stat_e, strength in equip.stats.items():
                if stat_e == stat:
                    base_value += strength
        return base_value
