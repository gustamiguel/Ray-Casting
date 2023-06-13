from config import *
import pygame, math

class Player:
    def __init__(self):
        self.x, self.y = pos_player
        self.angulo = ang_player
        
    @property
    def pos(self):
        return (self.x, self.y)   
        
    def movimento(self):
        sen_a = math.sin(self.angulo)
        cos_a = math.cos(self.angulo)
        
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_w]:
            self.x += vel_player * cos_a
            self.y += vel_player * sen_a
        if teclas[pygame.K_s]:
            self.x += -vel_player * cos_a
            self.y += -vel_player * sen_a
        if teclas[pygame.K_a]:
            self.x += vel_player * sen_a
            self.y += -vel_player * cos_a
        if teclas[pygame.K_d]:
            self.x += -vel_player * sen_a
            self.y += vel_player * cos_a
             
        # Ângulo   
            
        if teclas[pygame.K_LEFT]:
            self.angulo -= 0.02
        if teclas[pygame.K_RIGHT]:
            self.angulo += 0.02