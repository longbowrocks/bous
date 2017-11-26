#!/usr/bin/python3
# important things
import logging, sys
import random
import pygame
from pygame.locals import *
from keys import Keys
from game import Game

# TODO: create game screen
# TODO:

# init logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# includes critical, error, warning, info, debug :)

# init pygame whatnot
RESOLUTION = (854, 480)

# main classes
keys = Keys()


# ---- THE GAME ITSELF ---- #
def init_resources():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.mixer.quit()
    pygame.mixer.init(frequency=44100, buffer=0)

    # clock = pygame.time.Clock()
    #
    # sys_font = pygame.font.Font("./8514oem.fon", 20)

def game_loop():
    delta_t = clock.tick(60)

    # key stuff
    keys.update(pygame.event.get([KEYDOWN, KEYUP]))
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
    if keys.alt and keys.f4:
        pygame.quit()
        sys.exit()
    if keys.f11_toggle and not (screen.get_flags() & pygame.FULLSCREEN):
        pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)
    elif not keys.f11_toggle and screen.get_flags() & pygame.FULLSCREEN:
        pygame.display.set_mode(RESOLUTION)

    # update stuff
    if not keys.p_toggle:
        runTick(delta_t)

    # prepare next frame for display
    drawGame(screen)

    pygame.display.flip()

if __name__ == '__main__':
    # Init stuff
    init_resources()

    game = Game(keys)

    # Loop stuff
    while True:
        game.loop()
