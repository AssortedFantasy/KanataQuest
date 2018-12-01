import pygame as pg
# States.py is the definition file for game states!
# main_loops must be run in a game state.

# GLOBAL PARAMETERS
default_fps = 30
default_res = 640, 480
default_display_params = pg.RESIZABLE | 0


class GameState:
    """
    GameState is large file which serves to hold everything that is relevant to the game and running it.
    It serves to fill the function of not having huge numbers of global variables littered literally everywhere.
    """
    def __init__(self):
        self.is_active = True
        self.is_running = True
        self.fps = default_fps   # Probably don't set to 0
        self.res = default_res   # Width , Height
        self.display_params = default_display_params
        self.main_display = pg.display.get_surface()
        self.clock = pg.time.Clock()
