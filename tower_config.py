from constants import *

TOWERS =\
{
    # tour basique
    'red':\
            [
                { # Niveau 1
                    'shortcut':      pygame.K_q, 
                    'cost':          40,
                    'damage':        60,
                    'reload_time':   30,
                    'splash radius': 0,
                    'image_path':    'images/tour_pourpre.png',
                    'attack_range':  600,
                },

                { # Niveau 2
                    'shortcut':      pygame.K_q, 
                    'cost':          200,
                    'damage':        300,
                    'reload_time':   15,
                    'splash radius': 0,
                    'image_path':    'images/tour_pourpre_2.png',
                    'attack_range':  600,
                },

                { # Niveau 3
                    'shortcut':      pygame.K_q, 
                    'cost':          1000,
                    'damage':        600,
                    'reload_time':   5,
                    'splash radius': 0,
                    'image_path':    'images/tour_pourpre_3.png',
                    'attack_range':  600,
                },
            ],


    # dégâts de zone
    'orange':\
            [
                {
                    'shortcut':      pygame.K_s, 
                    'cost':          50,
                    'damage':        40,
                    'reload_time':   40,
                    'splash radius': 3 * GRID_WIDTH,
                    'attack_range':  300,
                    'image_path':    'images/tour_orange.png'
                },

                {
                    'shortcut':      pygame.K_s, 
                    'cost':          250,
                    'damage':        500,
                    'reload_time':   40,
                    'splash radius': 5 * GRID_WIDTH,
                    'attack_range':  300,
                    'image_path':    'images/tour_orange_2.png'
                },

                {
                    'shortcut':      pygame.K_s, 
                    'cost':          1200,
                    'damage':        800,
                    'reload_time':   40,
                    'splash radius': 10 * GRID_WIDTH,
                    'attack_range':  300,
                    'image_path':    'images/tour_orange_3.png'
                },
            ],

    # ralentit les creeps
    'blue':\
            [
                {
                    'shortcut':      pygame.K_d, 
                    'cost':          60,
                    'damage':        0,
                    'reload_time':   50,
                    'splash radius': 2 * GRID_WIDTH,
                    'attack_range':  200,
                    'slow_duration': 10 * FPS,
                    'slow_rate':     0.95,        # À chaque projectile, la vitesse est multipliée par slow_rate
                    'image_path':    'images/tour_bleue.png'
                },

                {
                    'shortcut':      pygame.K_d, 
                    'cost':          300,
                    'damage':        0,
                    'reload_time':   30,
                    'splash radius': 2 * GRID_WIDTH,
                    'attack_range':  300,
                    'slow_duration': 10 * FPS,
                    'slow_rate':     0.75,        
                    'image_path':    'images/tour_bleue_2.png'
                },

                {
                    'shortcut':      pygame.K_d, 
                    'cost':          1400,
                    'damage':        0,
                    'reload_time':   10,
                    'splash radius': 4 * GRID_WIDTH,
                    'attack_range':  400,
                    'slow_duration': 100 * FPS,
                    'slow_rate':     0.55,       
                    'image_path':    'images/tour_bleue_3.png'
                },
            ]
}
