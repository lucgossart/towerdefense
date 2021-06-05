from game.map.chemin  import NewPath
from .constants       import *

test_dict = [
    {
        'damage':                  1,
        'number_of_creeps':       15,
        'hp':                    200,
        'speed':                   2,
        'creep_income':            1,
        'start_income':            0,
        'path':              NewPath(CITY_WIDTH, WIDTH, HEIGHT).path,
        'image_path': PERE_NOEL_PATH,
        'width':         CREEP_WIDTH,
        'height':       CREEP_HEIGHT
    }
]
