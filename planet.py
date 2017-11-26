from gameColor import GameColor
import random, math
import logging
import pygame
from pointUtils import dist_squared
from constants import RESOLUTION, MIN_PLANET_SIZE, MAX_PLANET_SIZE, PLAYER_SIZE


class Planet():
    def __init__(self, radius, pos, color):
        self.radius = radius
        self.pos = pos
        self.gravity = 2.0
        self.color = color

    @staticmethod
    def create_non_overlapping(existing_planets):
        overlaps = True
        num_tries = 0
        while overlaps and num_tries < 100:
            num_tries += 1
            pos = Planet.get_random_legal_position()
            radius = random.randint(MIN_PLANET_SIZE, MAX_PLANET_SIZE)
            if pos[0] + radius + PLAYER_SIZE > RESOLUTION[0] or\
                pos[0] - radius - PLAYER_SIZE < 0:
                continue # planet overlaps with screen X bounds
            elif pos[1] + radius + PLAYER_SIZE > RESOLUTION[1] or\
                pos[1] - radius - PLAYER_SIZE < 0:
                continue # planet overlaps with screen Y bounds
            overlaps = False
            for planet in existing_planets:
                if dist_squared(pos, planet.pos) < (radius + planet.radius)**2:
                    overlaps = True
                    break
        if num_tries >= 100:
            logging.error("Tried to place a planet in an overpopulated system.")
            return Planet(MIN_PLANET_SIZE, (0, 0), GameColor.White)
        color = GameColor.Red
        return Planet(radius, pos, color)

    @staticmethod
    def get_random_legal_position():
        return (
            random.randint(0, RESOLUTION[0] - MIN_PLANET_SIZE),
            random.randint(0, RESOLUTION[1] - MIN_PLANET_SIZE)
        )

    @staticmethod
    def get_edge_pos(planet, angle):
        return (int(planet.pos[0] + planet.radius * math.cos(angle)),
                int(planet.pos[1] + planet.radius * math.sin(angle)))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
