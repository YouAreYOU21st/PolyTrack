from constants import *
from track_set_types import *

# Data for attached items to tiles and board in general
# Use these to build logic around the board

TerrainTypes = {
    'grass': TerrainSprites.grass,
    'tallgrass': TerrainSprites.tallgrass,
    'water': TerrainSprites.water, 
    'ice': TerrainSprites.ice
}

TrackTypes = [vertical, horizontal, left, right, ileft, iright]

ObstacleTypes = {
    'rock': ObstacleSprites.rock, 
    'sandrock': ObstacleSprites.sandrock, 
    'sadrock': ObstacleSprites.sadrock, 
    'tree': ObstacleSprites.tree, 
    'woodshack': ObstacleSprites.woodshack
}
SpawnObstacles = [
    'rock', 'sandrock', 'sadrock', 
    'tree', 'woodshack'
]

TrainTypes = {
    'default': {
        'image': TrainSprites.red_train, 
        'speed': 0.15,
    }, 
    'bullet': {
        'image': TrainSprites.gray_cargo,
        'speed': 0.25,
    }
}
TrainSpeed_Multipliers = {
    'fast_forward': {
        'multiplier': 8, 
        'active': False
    }, 
    # 'ice': {
    #     'multiplier': 0.9, 
    #     'active': False
    # }
}