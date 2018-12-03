import pygame as pg
import ctypes
import sys
from pathlib import Path
from . import states
from . import menus

# From https://gamedev.stackexchange.com/questions/105750/pygame-fullsreen-display-issue
if sys.platform == "win32":
    ctypes.windll.user32.SetProcessDPIAware()


def draw_loop(game: states.GameState, display):
    # Handles all drawing for the game!
    dx, dy = display.get_rect().center
    gx, gy = game.display_rect.center
    pg.display.get_surface().blit(game.main_display, (dx-gx, dy-gy))
    pg.display.flip()


def event_handler(game: states.GameState):
    # Handles certain events for the game, passes the rest into the deque in gamestate.
    game.event_queue.clear()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.is_running = False
        if event.type == pg.VIDEORESIZE:
            new_screen = pg.display.set_mode(event.size, game.display_params)
            new_screen.fill(game.background)
            game.screen_res_out_of_date = True
        if event.type in [pg.KEYDOWN, pg.KEYUP, pg.MOUSEMOTION, pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN]:
            game.event_queue.append(event)


# TODO: Move menu things, into update inside the state
def main(game):
    # Starts Main Menu
    menu = menus.MainMenu(game)
    display = pg.display.get_surface()
    while game.is_running:
        # pg.draw.circle(game.main_display, colours.Red, (0, 0), 100, 10)
        draw_loop(game, display)
        event_handler(game)
        game.update()
        """
        button_click = menu.is_clicked()
        if button_click:
            menu.menu_event(button_click)
        """
        game.clock.tick(game.fps)


# This is the entrance code for this file.
def launch():
    # First We need to run initialization.
    pg.init()

    # game is the GameState, it is very important
    game = states.GameState()

    # We first just make the display!
    screen = pg.display.set_mode()
    pg.display.set_caption("Katana Quest")
    screen.fill((255, 255, 255))
    pg.display.flip()
    game.fix_screen_resolution(force=True)

    # Now we launch the game!
    main(game)


if __name__ == "__main__":
    print("""Incorrectly launching the game, please launch using
    python on the main game directory itself!""")
    exit(-1)
