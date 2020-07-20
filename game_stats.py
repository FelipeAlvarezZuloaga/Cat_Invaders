########################################
#Puntuaciones#
########################################
class GameStats():
    
    def __init__(self, ai_settings):
        #Empezamos con la puntuación
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #Empezamos con un estado inactivo
        self.game_active = False
        
    def reset_stats(self):
        #Reiniciamos la puntuacion
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        
        