from constants import *

TOWERS =\
{
    # tour basique
    'red':\
            [
                { # Niveau 1
                    'shortcut':      pygame.K_q, 
                    'cost':          40,
                    'damage':        80,
                    'reload_time':   30,
                    'hp':            2,
                    'splash radius': 0,
                    'image_path':    'images/tour_pourpre.xcf',
                    'attack_range':  600,
                },

                { # Niveau 2
                    'shortcut':      pygame.K_q, 
                    'cost':          200,
                    'damage':        500,
                    'hp':            20,
                    'reload_time':   15,
                    'splash radius': 0,
                    'image_path':    'images/tour_pourpre_2.xcf',
                    'attack_range':  600,
                },

                { # Niveau 3
                    'shortcut':      pygame.K_q, 
                    'cost':          1000,
                    'damage':        1200,
                    'hp':            200,
                    'reload_time':   5,
                    'splash radius': 0,
                    'image_path':    'images/tour_pourpre_3.xcf',
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
                    'hp':            2,
                    'splash radius': 3 * GRID_WIDTH,
                    'attack_range':  300,
                    'image_path':    'images/tour_orange.xcf'
                },

                {
                    'shortcut':      pygame.K_s, 
                    'cost':          250,
                    'damage':        200,
                    'reload_time':   40,
                    'hp':            20,
                    'splash radius': 5 * GRID_WIDTH,
                    'attack_range':  300,
                    'image_path':    'images/tour_orange_2.xcf'
                },

                {
                    'shortcut':      pygame.K_s, 
                    'cost':          1200,
                    'damage':        500,
                    'reload_time':   40,
                    'hp':            200,
                    'splash radius': 10 * GRID_WIDTH,
                    'attack_range':  300,
                    'image_path':    'images/tour_orange_3.xcf'
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
                    'hp':            2,
                    'slow_duration': 10 * FPS,
                    'slow_rate':     0.95,        # À chaque projectile, la vitesse est multipliée par slow_rate
                    'image_path':    'images/tour_bleue.xcf'
                },

                {
                    'shortcut':      pygame.K_d, 
                    'cost':          300,
                    'damage':        0,
                    'reload_time':   30,
                    'splash radius': 2 * GRID_WIDTH,
                    'attack_range':  300,
                    'hp':            20,
                    'slow_duration': 10 * FPS,
                    'slow_rate':     0.75,        
                    'image_path':    'images/tour_bleue_2.xcf'
                },

                {
                    'shortcut':      pygame.K_d, 
                    'cost':          1400,
                    'damage':        0,
                    'reload_time':   10,
                    'splash radius': 4 * GRID_WIDTH,
                    'hp':            200,
                    'attack_range':  400,
                    'slow_duration': 100 * FPS,
                    'slow_rate':     0.55,       
                    'image_path':    'images/tour_bleue_3.xcf'
                },
            ],

    'yellow':\
            [
                {
                    'shortcut':      pygame.K_f, 
                    'cost':          150,
                    'hp':            2,
                    'image_path':    'images/tour_jaune.xcf'
                    ''
                }, 


            ],

    'rempart':\
            [
                {
                    'shortcut':      pygame.K_r, 
                    'cost':          150,
                    'hp':            20,
                    'image_path':    'images/rempart.png'
                },

                {
                    'shortcut':      pygame.K_r, 
                    'cost':          1500,
                    'hp':            600,
                    'image_path':    'images/rempart_2.png'
                },

                {
                    'shortcut':      pygame.K_r, 
                    'cost':          3500,
                    'hp':            12_000,
                    'image_path':    'images/rempart3.xcf'
                },
            ]
}
