from game import maps
import pygame as pg

im = pg.image.load("../assets/images/tmp.png")
test_level = maps.Levels(im)

print(test_level)
