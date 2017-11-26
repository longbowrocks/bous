import random, math
import pygame
from planet import Planet
from gameColor import GameColor

class Player:
    def __init__(self, planet, player_id):
        self.planet = planet
        self.color = random.choice(GameColor.PlayerColors)
        self.player_id = player_id

        self.angle = random.random() * 2 * math.pi
        self.pos = Planet.get_edge_pos(planet, self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, 10)
