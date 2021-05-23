import pygame

FONT       = "Perpetua"
FONT_SIZE  = 40
FONT_COLOR = (255, 125, 0) # (r, g, b)

BASE_HP   = 100
BASE_GOLD = 100

WIDTH, HEIGHT   = 640, 960
GRID_WIDTH      = 40
CREEP_WIDTH     = 100
CREEP_HEIGHT    = 100
PROJECTILE_SIZE = 40


FPS = 60
TOWER_HEIGHT = 60
TOWER_WIDTH  = 40

DOWN   = pygame.K_j
UP     = pygame.K_k
RIGHT  = pygame.K_l
LEFT   = pygame.K_h
DROP   = pygame.K_RETURN
CANCEL = pygame.K_ESCAPE


TOUR_POURPRE     = pygame.K_q
RED_TOWER_COST   = 10
RED_TOWER_DAMAGE = 20

CHEMIN_TOUR_POURPRE = 'images/tour_pourpre.png'

CURSOR_IMAGE        = pygame.image.load('images/cursor.png')
CURSOR_IMAGE        = pygame.transform.scale(CURSOR_IMAGE, (GRID_WIDTH, GRID_WIDTH))

PERE_NOEL           = pygame.image.load('images/png/Run (1).png')
PERE_NOEL           = pygame.transform.scale(PERE_NOEL, (CREEP_WIDTH, CREEP_HEIGHT))

SPEAR_IMAGE         = pygame.image.load('images/lance.png')
SPEAR_IMAGE         = pygame.transform.scale(SPEAR_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))


WAVES =\
[\
    {
        'number_of_creeps': 20,
        'hp': 200,
        'speed': 2
    },

    {
        'number_of_creeps': 30,
        'hp': 400,
        'speed': 2
    },

    {
        'number_of_creeps': 30,
        'hp': 400,
        'speed': 7
    }
]
