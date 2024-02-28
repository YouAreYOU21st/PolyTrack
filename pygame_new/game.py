# The top level of a scene, this is the state where you actually play

import pygame
import sys
import random
from constants import *
from board import Board
from track_box import Trackbox
from trains import Trains

from track_set_types import TrackSetTypes
from track_set import TrackSet

class Game:
    def __init__(self):
        pygame.init()
        self.game_surf = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.fps = pygame.time.Clock()

        self.board = Board()

        self.track_box = Trackbox()
        self.active_set = None

        self.trains = Trains()


    # Event control 
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: self.handle_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: self.handle_mouse_up(event)
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event)
            elif event.type == pygame.KEYDOWN:
                if self.active_set: self.handle_rotate()
            elif event.type == pygame.QUIT:
                self.quit_game()

    def handle_mouse_down(self, event):
        self.active_set = self.track_box.find_track_set(event.pos)

    def handle_mouse_up(self, event):
        if self.active_set != None:
            self.snap_set_to_board()
            self.active_set = None

    def handle_mouse_motion(self, event):
        if self.active_set != None:
            self.active_set.move(event.rel)
    
    def handle_rotate(self):
        self.active_set = self.track_box.rotate(self.active_set)
    

    # Game logic between components
    def find_tiles_under_tracks(self):
        track_positions = self.active_set.find_pos_of_tracks()
        tiles = []
        for position in track_positions:
            tile = self.board.find_tile_in_location(position)

            if tile == None: return None
            if not tile.is_open(): return None
            tiles.append(tile)
        return tiles

    def snap_set_to_board(self):
        hovered_tiles = self.find_tiles_under_tracks()
        if not hovered_tiles: 
            self.track_box.track_set_to_initial(self.active_set)
            return
        self.active_set.attach_tracks_to_tiles(hovered_tiles)
        self.track_box.remove_track_set(self.active_set)


    # Boilerplate to functionally update the game
    def quit_game(self):
        pygame.quit()
        sys.exit()
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.fps.tick(60)

    def update(self):
        self.track_box.update()

    def render(self):
        self.game_surf.fill(Colors.dark_gray)
        
        self.board.draw(self.game_surf)
        self.track_box.draw(self.game_surf)
        self.trains.draw(self.game_surf)

        pygame.display.update()