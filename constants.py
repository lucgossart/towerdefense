import pygame

BASE_HP   = 100
BASE_GOLD = 100

WIDTH, HEIGHT = 640, 960
GRID_WIDTH    = 40


FPS = 60
TOWER_HEIGHT = 60
TOWER_WIDTH  = 40

DOWN   = pygame.K_j
UP     = pygame.K_k
RIGHT  = pygame.K_l
LEFT   = pygame.K_h
DROP   = pygame.K_RETURN
CANCEL = pygame.K_ESCAPE


TOUR_POURPRE   = pygame.K_q
RED_TOWER_COST = 10

CHEMIN_TOUR_POURPRE = 'images/tour_pourpre.png'
CURSOR_IMAGE        = pygame.image.load('images/cursor.png')
CURSOR_IMAGE        = pygame.transform.scale(CURSOR_IMAGE, (GRID_WIDTH, GRID_WIDTH))
