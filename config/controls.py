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

            # Sélectionne le bâtiment sous le curseur ou construit
            # celui qui a été sélectionné
            LEFT_CLICK:      'select_or_build',
            pygame.K_RETURN: 'select_or_build',  # touche entrée

            pygame.K_u: 'upgrade_tower'     
        }


