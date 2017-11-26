import random
from planet import Planet
from gameColor import GameColor

class Player:
    def __init__(planets):
        self.planet = random.choice(planets)
        self.color = random.choice(GameColor.PlayerColors)

        self.angle = random.random() * 2 * math.pi
        self.pos = Planet.get_edge_pos(planet, angle)

    def draw(self, screen):
        screen.draw.circle(screen, self.color, self.pos, 10)
