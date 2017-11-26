#!/usr/bin/python3
# important things
import logging, sys
import random
import pygame
from pygame.locals import *
from keys import Keys
from game import Game
from constants import RESOLUTION

# xTODO: create game screen
# xTODO: draw planets
# xTODO: create a nonoverlapping system of planets
# xTODO: add game ticks
# TODO: draw moving arrow
# TODO: add planet gravity and make it affect arrows
# TODO: add collision between players, arrows, and planets
# TODO: draw path behind arrow
# TODO: draw path ahead of arrow
# TODO:

# init logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# includes critical, error, warning, info, debug :)

# main classes
keys = Keys()

# ---- THE GAME ITSELF ---- #
def init_resources():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.mixer.quit()
    pygame.mixer.init(frequency=44100, buffer=0)
    return screen

def key_stuff(screen):
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
        pass#runTick(delta_t)

if __name__ == '__main__':
    # Init stuff
    screen = init_resources()

    game = Game(keys)

    # Loop stuff
    while True:
        key_stuff(screen)

        game.loop()
        game.draw(screen)

        pygame.display.flip()
