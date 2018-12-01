import pygame as py
from . import colours

# GLOBAL PARAMETERS
fps = 30
res = width, height = 1280, 720


def main():
    pass


def event_loop():
    for event in py.event.get():
        pass


# This is the entrance code for this file.
def launch():
    py.init()
    GAME_RUN = True
    main_display = py.display.set_mode(res)
    try:
        splash = open("../assets/images/splash.png", mode="rb")
    except FileNotFoundError:
        print("Missing splash screen picture, using blank")

    main()


if __name__ == "__main__":
    print("""Incorrectly launching the game, please launch using
    python on the main game directory itself!""")
    exit(-1)
