import pygame
import math
from config import *
from player import *
from mapa import mapa_mundo
from ray_casting import ray_casting

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
CLOCK = pygame.time.Clock()
player = Player()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()          
    player.movimento()
    tela.fill(PRETO)
    
    ray_casting(tela, player.pos, player.angulo)
    
    pygame.draw.circle(tela, VERMELHO, (int(player.x), int(player.y)), 12)
    pygame.draw.line(tela, VERMELHO, player.pos, (player.x + LARGURA * math.cos(player.angulo), 
                                                  player.y + LARGURA * math.sin(player.angulo)))
    
    for x,y in mapa_mundo:
        pygame.draw.rect(tela, CINZAESCURO, (x, y, BLOCO, BLOCO), 2)
    
    pygame.display.flip()
    CLOCK.tick(FPS)