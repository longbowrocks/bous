from gameColor import GameColor
import random
from main import RESOLUTION

MIN_PLANET_SIZE = 20
MAX_PLANET_SIZE = 100

class Planet():
    def __init__(self, radius, pos, color):
        self.radius = radius
        self.pos = pos
        self.color = color

    @staticmethod
    def create_non_overlapping(existing_planets):
        radius = random.randint(MIN_PLANET_SIZE, MAX_PLANET_SIZE)
        pos = (random.randint(0, RESOLUTION[0]),random.randint(0, RESOLUTION[1]))
        color = GameColor.Red
        return Planet(radius, pos, color)
