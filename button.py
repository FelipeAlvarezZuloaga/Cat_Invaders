########################################
#Botones#
########################################

import pygame.font

class Button():
    
    def __init__(self, ai_settings, screen, msg):
        #Iniciamos con los atributos del boton
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #Tamaño del boton
        self.width, self.height = 200, 50
        self.button_color = (233, 123, 8)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,48)
        
        #Hagamos el objeto rectangulo del boton y centremoslo
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #El boton necesita prepararse solo una vez
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        #Convierte msg a una imagen renderizada y centra texto en el boton
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #Dibuja un boton en blanco y dibuja un mensaje
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        
        
        
        
        
        