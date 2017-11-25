import logging, sys
import random, math
import pygame
from pygame.locals import *
from gameColor import GameColor
from shadowedPressable import *
from textRenderer import TextRenderer

# TODO: create game screen
# TODO:

class Game:
  def __init__(self, WIN_TIME, COOLDOWN_TIME, STALE_TIME, TOTAL_TIME, FAILURE_TIME, keys, game_rect, shadow_dist, sys_font):
    # -- CONTROLS --
    self.keys = keys

    # -- GAMEPLAY --
    self.reset()
