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
        # init
        self.planets = self.init_planets(5)
        self.players = self.init_players(2)

        self.player = self.players[0]

    def init_planets(self, count):
        planets = []
        for idx in range(count):
            planets.append(Planet.create_non_overlapping(planets))
        return planets

    def init_players(self, count):
        return [pygame.Rect for idx in range(count)]

    def loop(self):
        pass

    def draw(self, screen):
        pass
