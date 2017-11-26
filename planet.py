from gameColor import GameColor
import random
from constants import RESOLUTION, MIN_PLANET_SIZE, MAX_PLANET_SIZE


class Planet():
    def __init__(self, radius, pos, color):
        self.radius = radius
        self.pos = pos
        self.gravity = 1.0
        self.color = color

    @staticmethod
    def create_non_overlapping(existing_planets):
        overlaps = True
        num_tries = 0
        while overlaps and num_tries < 100:
            pos = Planet.get_random_legal_position()
            radius = random.randint(MIN_PLANET_SIZE, MAX_PLANET_SIZE)
            num_tries += 1
            overlaps = False
        if num_tries >= 100:
            return Planet(MIN_PLANET_SIZE, (0, 0), GameColor.White)
        color = GameColor.Red
        return Planet(radius, pos, color)

    @staticmethod
    def get_random_legal_position():
        return (
            random.randint(0, RESOLUTION[0] - MIN_PLANET_SIZE),
            random.randint(0, RESOLUTION[1] - MIN_PLANET_SIZE)
        )

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
