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

    def reset(self):
        pass


    def get_planets(self, count):
        planets = []
        for idx in range(count):
            planets.append(Planet.create_non_overlapping(planets))
        return planets

    def get_player(self):
        return pygame.Rect

    def loop(self):
        planets = self.get_planets(5)
        players = [self.get_player() for i in range(2)]

        # and the rest
