from gameColor import GameColor
import random

MIN_PLANET_SIZE = 20
MAX_PLANET_SIZE = 100

class Planet():
    def __init__(self):
        pass

    @staticmethod
    def createNonOverlapping(existing_planets):
        radius = random.randint(MIN_PLANET_SIZE, MAX_PLANET_SIZE)
        pos = getPlanetPos()
        color = GameColor.Red
