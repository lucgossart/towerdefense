import pygame

BASE_HP   = 100
BASE_GOLD = 200

DOWN   = pygame.K_j
UP     = pygame.K_k
RIGHT  = pygame.K_l
LEFT   = pygame.K_h
DROP   = pygame.K_RETURN
CANCEL = pygame.K_ESCAPE


WAVES =\
[
    {
        'number_of_creeps': 15,
        'hp': 200,
        'speed': 2
    },

    {
        'number_of_creeps': 20,
        'hp': 400,
        'speed': 2
    },

    {
        'number_of_creeps': 20,
        'hp': 400,
        'speed': 3
    }
]

GRID_WIDTH      = 40
PROJECTILE_SIZE = 40

FPS = 60

TOWERS =\
{
    # tour basique
    'red': {
        'shortcut':      pygame.K_q, 
        'cost':          10,
        'damage':        60,
        'reload_time':   30,
        'splash radius': 0,
        'image_path':    'images/tour_pourpre.png',
        'attack_range':  600,
    },

    # dégâts de zone
    'orange': {
        'shortcut':      pygame.K_s, 
        'cost':          20,
        'damage':        40,
        'reload_time':   40,
        'splash radius': 5 * GRID_WIDTH,
        'attack_range':  300,
        'image_path':    'images/tour_orange.png'
    },

    # ralentit les creeps
    'blue': {
        'shortcut':      pygame.K_d, 
        'cost':          10,
        'damage':        0,
        'reload_time':   90,
        'splash radius': 2 * GRID_WIDTH,
        'attack_range':  200,
        'slow_duration': 10 * FPS,
        'slow_rate':     0.95,        # À chaque projectile, la vitesse est multipliée par slow_rate
        'image_path':    'images/tour_bleue.png'
    }
}

WIDTH, HEIGHT   = 640, 960
CREEP_WIDTH     = 100
CREEP_HEIGHT    = 100

CURSOR_IMAGE = pygame.image.load('images/cursor.png')
CURSOR_IMAGE = pygame.transform.scale(CURSOR_IMAGE, (GRID_WIDTH, GRID_WIDTH))

PERE_NOEL = pygame.image.load('images/png/Run (1).png')
PERE_NOEL = pygame.transform.scale(PERE_NOEL, (CREEP_WIDTH, CREEP_HEIGHT))

SPEAR_IMAGE = pygame.image.load('images/lance.png')
SPEAR_IMAGE = pygame.transform.scale(SPEAR_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))

BOMB_IMAGE = pygame.image.load('images/bomb.png')
BOMB_IMAGE = pygame.transform.scale(BOMB_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))

SHURIKEN_IMAGE = pygame.image.load('images/Air Shuriken.svg')
SHURIKEN_IMAGE = pygame.transform.scale(SHURIKEN_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))

FONT       = "Perpetua"
FONT_SIZE  = 40
FONT_COLOR = (255, 125, 0) # (r, g, b)



TOWER_HEIGHT = 60
TOWER_WIDTH  = 40
