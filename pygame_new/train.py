# handles individual train data

import pygame
from constants import *
import random
import math

class Train:
    def __init__(self, deg, spd, x, y, direction, set, start, end):
         # pygame.Surface([width,height]) controls size of the train
        self.surface = pygame.Surface([60 * (TRACK_WIDTH/50), (TRACK_HEIGHT - 2 * (TRACK_HEIGHT/50))])
        self.degree = deg
        self.speed = spd
        self.set = set
        
        # center of the train x and y location
        self.x_center_adjustment = abs(pygame.Surface.get_width(self.surface) / 2 * math.cos(math.radians(self.degree)) + pygame.Surface.get_height(self.surface) / 2 * math.sin(math.radians(self.degree)))
        self.y_center_adjustment = abs(pygame.Surface.get_height(self.surface) / 2 * math.cos(math.radians(self.degree)) + pygame.Surface.get_width(self.surface) / 2 * math.sin(math.radians(self.degree)))
        
        self.x = board_x + OUTER_GAP + x * (TRACK_WIDTH + INNER_GAP) + self.x_center_adjustment
        self.y = board_y + OUTER_GAP + y * (TRACK_HEIGHT + INNER_GAP) + self.y_center_adjustment
        if self.degree == 180:
            self.x -= pygame.Surface.get_width(self.surface) - TRACK_WIDTH - INNER_GAP
        if self.degree == 90:
            self.y -= pygame.Surface.get_width(self.surface) - TRACK_HEIGHT - INNER_GAP

        # start and end location
        self.start = start
        self.end = end

        # there are three option for this "foward", clockwise", and "counter-clockwise"
        # "foward" makes the train keep moving in the direction its facing
        # "clockwise" makes the train turn clockwise
        # "counter-clockwise" makes the train turn counter-clockwise
        self.direction = direction

        self.rotate = pygame.transform.rotate(self.surface, self.degree)
        self.rotate_rect = self.rotate.get_rect(center = (self.x, self.y))

        # makes it background it on transparent so it looks like it turning and it would look like it expanding
        self.surface.set_colorkey(Colors.white)

        # train image
        #image = TrainSprites.red_train.convert_alpha()
        #image = pygame.transform.smoothscale(image, (56, 48)) 
        #self.surface.blit(image, (0,0))
        
        image = random.choice(TrainSprites.random_train_choice).convert_alpha()
        image = pygame.transform.smoothscale(image, [60 * (TRACK_WIDTH/50), 48 * (TRACK_HEIGHT/50)])
        self.surface.blit(image, (0,0))