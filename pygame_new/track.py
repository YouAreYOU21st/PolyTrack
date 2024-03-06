# Handles tracks

from constants import *

class Track:
    def __init__(self, rect, data):
        self.type = "track"
        self.rect = rect
        self.data = data
        self.image = data['sprite']
        self.d0 = data['directions'][0]
        self.d90 = data['directions'][1]
        self.d180 = data['directions'][2]
        self.d270 = data['directions'][3]

        self.relations = []

    # Knows what tracks are next to it in the set
    # Turned out unnecessary for movement but could be useful maybe?
    def set_relation(self, track):
        self.relations.append(track)

    def move(self, relative_position):
        self.rect.move_ip(relative_position)
