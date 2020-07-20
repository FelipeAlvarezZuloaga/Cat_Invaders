########################################
#Nave#
########################################
import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        #Iniciamos la nave y su posición
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Cargamos la nave
        self.image = pygame.image.load(r'C:\Users\52554\Desktop/CorgoEspacial3.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()
        
        #Empezamos con la nave en la parte inferior centrada
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom        
        
        #Guardamos un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)
        
        #Banderas Controladoras
        self.moving_right = False
        self.moving_left = False 
        
        
    def update(self):
        #Cambiamos la posición dependiendo de las banderas
        #Actualizamos el movimiento con base en el centro
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor 
            
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Actualizamos el centro
        self.rect.centerx = self.center
        
    def blitme(self):
        #Dibuja la nave
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        #Centra la nave
        self.center = self.screen_rect.centerx
        