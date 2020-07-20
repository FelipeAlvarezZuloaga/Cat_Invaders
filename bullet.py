########################################
#Balas#
########################################

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ai_settings, screen, ship):
        #Creamos un objeto bala en la posición de la nave
        super(Bullet, self).__init__()
        self.screen = screen
        
        #Creamos una bala en (0,0) y después la movemos a la posición correcta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Guardamos la posicion de la bala con un valor decimal
        self.y = float(self.rect.y)     
        
        self.color=ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        #Movemos la bala en la pantalla
        #Actualizamos la posicion decimal de la bala
        self.y -= self.speed_factor
        #Actualizamos la posicion de la bala
        self.rect.y = self.y
        
    def draw_bullet(self):
        #Diuja la bala
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        