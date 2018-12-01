import pygame as pg
from . import states
from . import colours


def draw_loop(game):
    # Handles all drawing for the game!
    pass


def event_handler(game: states.GameState):
    # Handles all events for the game!
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.is_running = False
        if event.type == pg.ACTIVEEVENT:
            print(event)
        if event.type == pg.VIDEORESIZE:
            pg.display.set_mode(event.size, game.display_params)
            game.res = event.size


def main(game):
    while game.is_running:
        event_handler(game)
        game.clock.tick(game.fps)


# This is the entrance code for this file.
def launch():
    # First We need to run initialization.
    pg.init()
    try:
        splash_file = open("./assets/images/splash.png", mode="rb")
    except FileNotFoundError:
        splash_file = None
        print("Error: Missing splash screen picture! Is the assets folder missing or path incorrect?")
        exit(-1)

    # First we display a splash screen
    splash_screen = pg.image.load(splash_file)
    main_display = pg.display.set_mode(splash_screen.get_rect().size)
    main_display.blit(splash_screen, main_display.get_rect())
    pg.display.flip()

    # Then we create a new GameState object, this is going to be the runtime.
    game = states.GameState()

    # Then we launch it!
    main(game)


if __name__ == "__main__":
    print("""Incorrectly launching the game, please launch using
    python on the main game directory itself!""")
    exit(-1)
