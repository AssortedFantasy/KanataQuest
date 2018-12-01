import pygame as pg
from . import colours

# Use this clock for everything which is that needs to be done!
main_clock = pg.time.Clock()

# GLOBAL PARAMETERS
default_fps = 30
default_res = 640, 480
default_display_params = pg.RESIZABLE | 0


def main():
    run_game = True
    while run_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_game = False
            if event.type == pg.VIDEORESIZE:
                pg.display.set_mode(event.size, default_display_params)

        pg.display.flip()
        main_clock.tick(default_fps)


# This is the entrance code for this file.
def launch():
    pg.init()

    try:
        splash_file = open("./assets/images/splash.png", mode="rb")
    except FileNotFoundError:
        splash_file = None
        print("Missing splash screen picture! Is the assets folder missing?")
        exit(-1)

    splash_screen = pg.image.load(splash_file)
    main_display = pg.display.set_mode(default_res, default_display_params)

    pg.Surface.blit(splash_screen, main_display, main_display.get_rect())
    pg.display.flip()
    main()


if __name__ == "__main__":
    print("""Incorrectly launching the game, please launch using
    python on the main game directory itself!""")
    exit(-1)
