import pygame as pg
import ctypes
import sys
from pathlib import Path
from . import states


# From https://gamedev.stackexchange.com/questions/105750/pygame-fullsreen-display-issue
if sys.platform == "win32":
    ctypes.windll.user32.SetProcessDPIAware()
splash_location = Path("./assets/images/splash.png")


def draw_loop(game_state: states.GameState):
    """
    The draw loop takes whatever is the current screen in the game and draws it to the screen
    """
    screen = pg.display.get_surface()
    dx, dy = screen.get_rect().center
    gx, gy = game_state.display_rect.center
    pg.display.get_surface().blit(game_state.main_display, (dx - gx, dy - gy))
    pg.display.flip()


def event_handler(game_state: states.GameState):
    """
    The event handler first clears the games event queue, then puts copies of all events which are on the event loop
    onto the games internal copy of the event loop.

    With the exception of the QUIT and VIDEORESIZE types of events, which it handles itself.
    """
    for event in pg.event.get():
        game_state.event_queue.clear()
        if event.type == pg.QUIT:
            game_state.is_running = False
        elif event.type == pg.VIDEORESIZE:
            new_screen = pg.display.set_mode(event.size, game_state.display_params)
            new_screen.fill(game_state.background)
            game_state.screen_res_out_of_date = True
        else:
            game_state.event_queue.append(event)


def main(game):
    while game.is_running:
        draw_loop(game)
        event_handler(game)
        game.update()
        game.clock.tick(game.fps)


# This is the entrance code for this file.
def launch():
    # First We need to run initialization.
    pg.init()

    try:
        splash_file = open(splash_location, mode="rb")
    except FileNotFoundError:
        splash_file = None
        print("Error: Missing splash screen picture! Is the assets folder missing or path incorrect?")
        exit(-1)

    # game is the GameState, it is very important
    game = states.GameState()

    # We first just make the display!
    screen = pg.display.set_mode()
    pg.display.set_caption("Katana Quest")
    screen.fill((255, 255, 255))
    pg.display.flip()

    # Now we write the splash screen to the game!
    game.fix_screen_resolution(force=True)
    splash_screen = pg.image.load(splash_file)
    sx, sy = splash_screen.get_rect().center
    gx, gy = game.main_display.get_rect().center
    game.main_display.blit(splash_screen, (gx-sx, gy-sy))

    # Now we launch the game!
    main(game)


if __name__ == "__main__":
    print("""Incorrectly launching the game, please launch using
    python on the main game directory itself!""")
    exit(-1)
