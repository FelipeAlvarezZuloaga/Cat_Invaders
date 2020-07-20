########################################
#Funciones del juego#
########################################

#
import sound_effects as se
#

import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #Responde al presionar las teclas
    if event.key == pygame.K_RIGHT:
        #Nos movemos a la derecha
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Nos movemos a la derecha
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        pygame.display.quit(), sys.exit()
       
def fire_bullet(ai_settings, screen, ship, bullets):
    #Dispara una bala si no se ha llegado al limite de balas
    #Crea una bala y la añade al grupo balas
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
        
def check_keyup_events(event, ship):
    #Responde al soltar las teclas
    if event.key == pygame.K_RIGHT:
        ship.moving_right =False
    if event.key == pygame.K_LEFT:
        ship.moving_left =False
                
        

def check_events(ai_settings, screen, stats, play_button, ship, aliens,
                 bullets):
    #Responder cuando uses el mouse o teclado
    
    #Cerrar ventana cuando des click en x
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit(), sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                    
                
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)                
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, play_button, ship,
                                  aliens, bullets, mouse_x, mouse_y)
                
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    #Empezamos un juego nuevo cuando le damos click al boton
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Reiniciamos las características iniciales
        ai_settings.initialize_dynamic_settings()
        #Escondemos el mouse
        pygame.mouse.set_visible(False)
        #Reiniciamos las condiciones iniciales del juego
        stats.reset_stats()
        stats.game_active = True            
        
        #Reiniciamos los aliens y balas
        aliens.empty()
        bullets.empty()
        
        #Creamos una nueva flota y centramos la nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
                
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    #Actualiza las imagenes en la pantalla 
    
    #Redibujamos la pantalla cada paso 
    screen.fill(ai_settings.bg_color)
    #Redibujamos las balas junto a la nave y aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    #Dibuja la informacion de los puntos
    sb.show_score()
    
    #Dibujamos el boton si el juego esta inactivo
    if not stats.game_active:
        play_button.draw_button()
    
    #Actualiza la pantalla 
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #Actualiza la posicion de las balas y se deshace de las balas viejas
    #Posicion de las balas
    bullets.update()
    
    #Eliminamos las balas que llegan hasta arriba
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets):
    #Checa si alguna bala le dio a un alien
    #En caso de ser así, elimina ambos
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        se.alien_sound.play()
        stats.score += ai_settings.alien_points
        sb.prep_score()
     
    if len(aliens) == 0:
        #Destruye las balas existentes y crea una nueva flota
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
    
    

def get_number_aliens_x(ai_settings, alien_width):
    #Determina cuantos aliens caben en la fila
    available_space_x = ai_settings.screen_width -  2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    #Determina el numero de filas que caben en pantalla
    available_space_y = (ai_settings.screen_height - 
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height) )
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Crea un alien y lo pone en la fila
    alien = Alien(ai_settings, screen) 
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)    
    
def create_fleet(ai_settings, screen, ship, aliens):
    #Crea una flota de aliens
    alien = Alien(ai_settings, screen) 
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    #Creamos la primera fila
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):    
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)
    
def check_fleet_edges(ai_settings, aliens):
    #Cambia la direccion si el alien llego al borde
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction (ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    #Baja la flota y cambia la direccion
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    #Pierdes 1 vida cuando le pegan a la nave
    #stats.ships_left -= 1
    if stats.ai_settings.ship_limit > 0:
        stats.ai_settings.ship_limit -= 1
        #Reiniciamos los aliens y balas
        aliens.empty()
        bullets.empty()
        
        #Creamos unanueva flota y una nueva nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        #Pausamos 
        sleep(0.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    #Checa si algun alien llegó a la parte de abajo
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    #Checa si la flota esta en el borde y actualiza la posicion
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    #Checa si perdiste
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
