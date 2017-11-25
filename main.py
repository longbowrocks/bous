#!/usr/bin/python3
# WHY DO YOU HATE IMPORTING THINGS?
# ---- NECESSARY EVILS ---- #
# important things
import logging, sys
import random
import pygame
from pygame.locals import *
from keys import Keys

# TODO: create game screen
# TODO:

# init logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# includes critical, error, warning, info, debug :)

# init pygame whatnot
RESOLUTION = (854, 480)

# ---- THE GAME ITSELF ---- #
def initResources():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.mixer.quit()
    pygame.mixer.init(frequency=44100, buffer=0)

    clock = pygame.time.Clock()

    sys_font = pygame.font.Font("./8514oem.fon", 20)

# visual params
p_list_rect = pygame.Rect((0, 0), (screen.get_width(), screen.get_height()))
scoreboard_rect = pygame.Rect((screen.get_width() * 0.3125, screen.get_height() * 0.1), (screen.get_width() * 0.375, screen.get_height() * 0.8))

top_rect = pygame.Rect(0, 0, screen.get_width(), screen.get_height() * 0.2)
top_rect_left = pygame.Rect(0, 0, screen.get_width() / 2, top_rect.height)
top_rect_right = pygame.Rect(screen.get_width() / 2, 0, screen.get_width() / 2, top_rect.height)

game_rect = pygame.Rect(0, top_rect.bottom, screen.get_width(), screen.get_height() * 0.7)

bottom_rect = pygame.Rect(0, game_rect.bottom, screen.get_width(), screen.get_height() * 0.1)

shadow_dist = screen.get_width() * 0.005

# main classes
keys = Keys()

def gameLoop():
  delta_t = clock.tick(60)

  # key stuff
  keys.update(pygame.event.get([KEYDOWN, KEYUP]), lambda char: match.p_list.input(char))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  if keys.alt and keys.f4:
    pygame.quit()
    sys.exit()
  if keys.f11_toggle and not (screen.get_flags() & pygame.FULLSCREEN):
    pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)
  elif not keys.f11_toggle and screen.get_flags() & pygame.FULLSCREEN:
    pygame.display.set_mode(RESOLUTION)

  # update stuff
  if not keys.p_toggle:
    runTick(delta_t)

  # prepare next frame for display
  drawGame(screen)

  pygame.display.flip()

if __name__ == '__main__':
    while True:
      gameLoop()
