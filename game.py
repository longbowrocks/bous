import logging, sys
import random, math
import pygame
from pygame.locals import *
from gameColor import GameColor
from planet import Planet
from arrow import Arrow
from player import Player

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
        self.arrows = [Arrow((50,50), (0.1,0.1), self.players[0].color, self.players[0].player_id)]

        self.player = self.players[0]

    def init_planets(self, count):
        planets = []
        for idx in range(count):
            planets.append(Planet.create_non_overlapping(planets))
        return planets

    def init_players(self, count):
        return [Player(random.choice(self.planets), idx) for idx in range(count)]

    def loop(self):
        for arrow in self.arrows:
            arrow.tick(self.planets)

        #for player in self.players:
        #    player.tick()

        # Check collisions
        for arrow in self.arrows:
            for player in self.players:
                if arrow.collides_player(player):
                    pass # end flight/turn/life
            for planet in self.planets:
                if arrow.collides_planet(planet):
                    pass # end flight/turn

    def draw(self, screen):
        for planet in self.planets:
            planet.draw(screen)

        for arrow in self.arrows:
            arrow.draw(screen)

        for player in self.players:
            player.draw(screen)
