import pygame

LEFT_CLICK  = 1
RIGHT_CLICK = 2

commands =\
        {
            pygame.K_j: 'cursor_down',
            pygame.K_k: 'cursor_up',
            pygame.K_l: 'cursor_right',
            pygame.K_h: 'cursor_left',
            pygame.K_u: 'upgrade',

            pygame.K_q: 'prepare_red_tower',
            pygame.K_s: 'prepare_orange_tower',
            pygame.K_d: 'prepare_blue_tower',

            # Sélectionne le bâtiment sous le curseur ou construit
            # celui qui a été sélectionné
            LEFT_CLICK:      'select_or_build',
            pygame.K_RETURN: 'select_or_build',            # touche entrée

            # retire la sélection fluo et l'éventuel bâtiment en préparation sous le curseur
            pygame.K_ESCAPE: 'unprepare_and_or_deselect',  
            pygame.K_u:      'upgrade'                     #  
        }


