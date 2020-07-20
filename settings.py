########################################
#Ajustes#
########################################

class Settings():
#Una clase para poner los ajustes de alien invasion#

    def __init__(self):
    
        #Parametros de la ventana
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        
        #Parametros de la nave
        #Numero de vidas de la nave
        self.ship_limit = 3
        
        #Parametros de la bala
        self.bullet_width= 3
        self.bullet_height= 15
        self.bullet_color = (10, 229, 8)
        self.bullets_allowed = 3
        
        #Parametros del alien
        self.fleet_drop_speed = 10
        
        #Que tan rápido queremos que se mueva el juego
        self.speedup_scale = 1.1 
        self.initialize_dynamic_settings()
       
        #Puntos por alien
        self.alien_points = 50
       
    def initialize_dynamic_settings(self):
        #Configuraciones que iran cambiando en el juego
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor =1
        # 1 representa moverse a la derecha y -1 a la izq
        self.fleet_direction=1
        
    def increase_speed(self):
        #Aumenta los valores iniciales
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
    
        