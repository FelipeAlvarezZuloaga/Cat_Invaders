########################################
#Space Invaders#
########################################

import pygame

pygame.mixer.init()

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    #Iniciamos el juego y creamos yna ventana 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
       
    #Nombre de la ventana
    pygame.display.set_caption("Cats Invading")
    
    #Creamos el boton de inicio
    play_button = Button(ai_settings, screen, "Jugar")
    
    #Guardemos la puntuacion
    stats = GameStats(ai_settings)
    
    #Creamos la tabla de puntos
    sb = Scoreboard(ai_settings, screen, stats)
    
    #Construimos la nave
    ship=Ship(ai_settings, screen)
    
    #Hacemos un grupo para guardar las balas
    bullets = Group()
    
    #Hacemos un grupo de aliens
    aliens = Group()
    
    #Creamos una flota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Loop principal
    while True :
        
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
              
run_game()
    