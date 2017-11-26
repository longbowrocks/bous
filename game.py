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
        self.planets = init_planets()
        self.players = init_players()

        self.player = players[0]

    def init_planets(self, count):
        return [Planet.create_non_overlapping(planets) for idx in count]

    def init_players(self, count):
        return [pygame.Rect for idx in count]

    def loop(self):
        #

    def draw(self, screen):
