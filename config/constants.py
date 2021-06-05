import pygame



BASE_HP   = 100
BASE_GOLD = 1000

GRID_WIDTH      = 40
PROJECTILE_SIZE = 40

TOWER_HEIGHT = 60
TOWER_WIDTH  = 40

BUILDING_WIDTH  = 40
BUILDING_HEIGHT = 40

FPS = 60

WIDTH, HEIGHT = 1000, 1000
CITY_WIDTH    = 100
CREEP_WIDTH   = 100
CREEP_HEIGHT  = 100

BACKGROUND  = pygame.image.load('images/map.jpg')
BACKGROUND  = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

CURSOR_IMAGE = pygame.image.load('images/cursor.png')
CURSOR_IMAGE = pygame.transform.scale(CURSOR_IMAGE, (GRID_WIDTH, GRID_WIDTH))

PERE_NOEL_PATH = 'images/png/Run (1).png'
PERE_NOEL = pygame.image.load(PERE_NOEL_PATH)
PERE_NOEL = pygame.transform.scale(PERE_NOEL, (CREEP_WIDTH, CREEP_HEIGHT))

SPEAR_IMAGE = pygame.image.load('images/lance.png')
SPEAR_IMAGE = pygame.transform.scale(SPEAR_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))

BOMB_IMAGE = pygame.image.load('images/bomb.png')
BOMB_IMAGE = pygame.transform.scale(BOMB_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))

SHURIKEN_IMAGE = pygame.image.load('images/Air Shuriken.svg')
SHURIKEN_IMAGE = pygame.transform.scale(SHURIKEN_IMAGE, (PROJECTILE_SIZE, PROJECTILE_SIZE))

SELECTED_TOWER = pygame.image.load('images/selection_cursor.png')
SELECTED_TOWER = pygame.transform.scale(SELECTED_TOWER, (TOWER_WIDTH + 10, TOWER_HEIGHT + 10))

FONT       = "Perpetua"
FONT_SIZE  = 40
FONT_COLOR = (255, 125, 0) # (r, g, b)

IMAGES_LIST = [CURSOR_IMAGE, PERE_NOEL, SPEAR_IMAGE, BOMB_IMAGE, SHURIKEN_IMAGE, SELECTED_TOWER]



