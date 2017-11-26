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

        self.player = self.players[0]
        self.arrow = self.init_arrows(self.player)

    def init_planets(self, count):
        planets = []
        for idx in range(count):
            planets.append(Planet.create_non_overlapping(planets))
        return planets

    def init_players(self, count):
        return [Player(random.choice(self.planets), idx) for idx in range(count)]

    def init_arrows(self, player):
        return Arrow((50,50), (random.random()*0.2,random.random()*0.2), player.color, player.player_id)

    def loop(self):
        self.arrow.tick(self.planets)

        #for player in self.players:
        #    player.tick()

        # Check collisions
        for player in self.players:
            if self.arrow.collides_player(player):
                pass # end flight/turn/life
        for planet in self.planets:
            if self.arrow.collides_planet(planet):
                self.arrow = self.init_arrows(self.player) # end flight/turn

    def draw(self, screen):
        for planet in self.planets:
            planet.draw(screen)

        self.arrow.draw(screen)

        for player in self.players:
            player.draw(screen)
