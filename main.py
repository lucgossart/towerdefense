import pygame

from game.game        import Game
from config.constants import *
from config.controls  import commands
from config.units     import test_dict

from game.entities.units.units import Creep




def main():

    pygame.init()
    window      = pygame.display.set_mode((WIDTH, HEIGHT))
    game        = Game()

    for image in IMAGES_LIST:
        image.convert()

    game.set_cursor(CURSOR_IMAGE, GRID_WIDTH, WIDTH, HEIGHT)
    game.set_displayer(window, BACKGROUND, SELECTED_TOWER)
    game.set_player(BASE_HP, BASE_GOLD)
    game.set_controller(commands)

    
    Creep(test_dict, pygame.Rect(800, 500, 1,1))
    game.main_loop(FPS)
    
    pygame.quit()


if __name__ == '__main__':
    main()
