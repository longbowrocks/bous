from pointUtils import dist, diff, to_int
from constants import GRAVITY_FALLOFF_EXP
import pygame


class Arrow():
    def __init__(self, pos, velocity, color, player_id):
        self.pos = pos
        self.velocity = velocity
        self.color = color
        self.player_id = player_id
        self.history = []

    def tick(self, planets):
        self.history += self.pos

        a_x = 0.0
        a_y = 0.0
        for planet in planets:
            pdist = dist(self.pos, planet.pos)
            acc = planet.gravity / pdist**GRAVITY_FALLOFF_EXP
            a_x += diff(planet.pos, self.pos)[0] / pdist * acc
            a_y += diff(planet.pos, self.pos)[1] / pdist * acc

        self.velocity = (
            self.velocity[0] + a_x,
            self.velocity[1] + a_y
        )

        self.pos = (
            self.pos[0] + self.velocity[0],
            self.pos[1] + self.velocity[1]
        )

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, to_int(self.pos), 2)

    def collides_player(self, player):
        return False

    def collides_planet(self, planet):
        if dist(self.pos, planet.pos) < planet.radius:
            return True
        return False
