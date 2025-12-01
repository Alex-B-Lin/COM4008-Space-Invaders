
#%reset -f

##imorts
import pygame 
from bullet_class import Bullet
from enemy_class import Enemy

##setup
#%reset -f

##setup
import pygame 

pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode([500,500])
screen.fill([0,0,0]) # black background

##constant variable deleration
PLAYER_Y=450





##variable decleration
player_x = 175
#enemy_x=-1
#enemy_y=20







#enemy array creation fucntion
#def create_enemies():
#    aliens = []    
#    for x in range(0, 400, 50):
#        for y in range(0, 200, 50):
#            alien=Enemy(20,20,pygame.image.load("Images\SI_enemy1.jpg"),50,50)
#            alien.image = pygame.transform.scale(alien.image, (50, 50))
#            aliens.append(alien)
#            screen.blit(alien.image, (x, y))
#    return aliens

#aliens = create_enemies()  

#def move_enemies(aliens):
#    for alien in aliens:
#        alien.move()
#        # alien.draw()
#        screen.blit(alien.image, (alien.y, alien.x))

##player character creation fucntion
def player_creation():
    player_image=pygame.image.load("Images\SI_player.png")
    player_image = pygame.transform.scale(player_image, (175, 50))
    screen.blit(player_image, (player_x, PLAYER_Y))   





##player shoot function
def player_shoot():
    bullet=Bullet(player_x,PLAYER_Y,"Images\SI_bullet.png",100,100,screen)
    bullet.bullet_move()



##game running
running = True
while running: 
    player_creation()
    ##user interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
                player_x += 5

            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                print("Space key pressed")
                player_shoot()
                pygame.time.wait(500)
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                print("Space key pressed")
                player_shoot()
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
    ##player boundry detection 
    if player_x<-60:
        player_x+=5
    elif player_x>385:
        player_x-=5
    
    
    
    
    
    ##enemy character creation
    #enemy1_image=pygame.image.load("Images\SI_enemy1.jpg")
    #enemy1_image = pygame.transform.scale(enemy1_image, (75,60))


    
    #move_enemies(aliens)

    
    ##update screen
    pygame.display.flip()


pygame.quit()
pygame.display.quit()
#del screen  


