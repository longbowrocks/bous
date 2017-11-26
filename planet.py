from gameColor import GameColor
import random
from constants import RESOLUTION, MIN_PLANET_SIZE, MAX_PLANET_SIZE


class Planet():
    def __init__(self, radius, pos, color):
        self.radius = radius
        self.pos = pos
        self.color = color

    @staticmethod
    def create_non_overlapping(existing_planets):
        overlaps = True
        while overlaps and num_tries < 100:
            pos = get_random_legal_position()
            radius = random.randint(MIN_PLANET_SIZE, MAX_PLANET_SIZE)
            overlaps = False
        if num_tries >= 100:
            return Planet(MIN_PLANET_SIZE, (0, 0), GameColor.White)
        color = GameColor.Red
        return Planet(radius, pos, color)

    @staticmethod
    def get_random_position():
        return (
            random.randint(0, RESOLUTION[0] - MIN_PLANET_SIZE),
            random.randint(0, RESOLUTION[1] - MIN_PLANET_SIZE)
        )
