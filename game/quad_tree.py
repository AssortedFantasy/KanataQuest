from collections import deque
import pygame as pg


# Quad Tree based on Pygame Rects
class QuadTree:
    def __init__(self, rect: pg.Rect, capacity):
        self.rect = rect.copy()
        self.points = []  # Tuple of item, x, y
        self.div = []
        self.capacity = capacity

    def add_item(self, item, x, y):
        if self.rect.collidepoint(x, y):
            for child in self.div:
                if child.add_item(item, x, y):
                    return True
            self.points.append((item, x, y))
            if len(self.points) == self.capacity:
                self.subDivide()
        else:
            return False

    # Return all items inside a given rect object!
    def query(self, rect: pg.Rect, _container=None):
        if _container is None:
            _container = deque()

        for item, x, y in self.points:
            if rect.collidepoint(x, y):
                _container.append(item)

        for child in self.div:
            child.query(rect, _container=_container)
        return _container

    def subDivide(self):
        width = self.rect.width/2
        height = self.rect.height/2

        r0 = pg.Rect(self.rect.topleft, width, height)
        r1 = pg.Rect(self.rect.midtop, width, height)
        r2 = pg.Rect(self.rect.midleft, width, height)
        r3 = pg.Rect(self.rect.center, width, height)
        self.div.extend([
            QuadTree(r0, self.capacity),
            QuadTree(r1, self.capacity),
            QuadTree(r2, self.capacity),
            QuadTree(r3, self.capacity),
        ])
