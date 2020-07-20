########################################
#Aliens#
########################################

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Crearemos una clase para representar un alien de la flota
    
    def __init__(self, ai_settings, screen):
        #Inicia el alien y su posición de inicio 
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Cargamos la imagen del alien y su atributo rectangulo
        self.image = pygame.image.load(r'C:\Users\52554\Desktop/GatoEspacial3.bmp')
        self.rect = self.image.get_rect()
        
        #Los aliens aparecen en la esquina superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Guardamos la posicion del alien
        self.x = float(self.rect.x)
        
    def blitme(self):
        #Dibujamos el alien en su posición actual
        self.screen.blit(self.image, self.rect)
     
    def check_edges(self):
        #Regresa True si el alien esta en la orilla
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
     
    def update(self):
        #Mueve el alien a la derecha
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)
        
        self.rect.x= self.x





