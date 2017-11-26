import logging, sys
import random, math
import pygame
from pygame.locals import *
from gameColor import GameColor
from planet import Planet

class Game:
    def __init__(self, keys):
        # -- CONTROLS --
        self.keys = keys

        # -- GAMEPLAY --
        self.reset()

    def loop(self):
        planets = get_planets(5)
        players = [get_player() for i in range(2)]

        # and the rest
