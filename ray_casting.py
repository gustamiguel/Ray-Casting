import pygame
from config import *
from mapa import mapa_mundo

def ray_casting(tela,  pos_player, ang_player):
    angulo_atual = ang_player - METADE_FOV
    xo, yo = pos_player
    for ray in range(NUM_RAIOS):
        sen_a = math.sin(angulo_atual)
        cos_a = math.cos(angulo_atual)
        for profundidade in range(PROFUNDIDADE_MAX):
            x = xo + profundidade * cos_a
            y = yo + profundidade * sen_a
            pygame.draw.line(tela, CINZAESCURO, pos_player,  (x, y), 2)   
            if (x // BLOCO * BLOCO, y // BLOCO * BLOCO) in mapa_mundo:
                break
        angulo_atual += ANGULO_DELTA