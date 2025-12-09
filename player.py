##imorts
import pygame 
from bullet_class import Bullet
from enemy_class import Enemy

##setup
pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode((500,500))
screen.fill([0,0,0]) # black background
colour = (255, 0, 0)

##constant variable deleration
PLAYER_Y=450

##variable decleration
player_x = 175
player_lives=3
bullet=None
bullet_list=[]

##player character creation fucntion
def player_creation():
    player_image=pygame.image.load("Images\SI_player.png")
    player_image = pygame.transform.scale(player_image, (175, 50))
    screen.blit(player_image, (player_x, PLAYER_Y))   


##player shoot function
def player_shoot():
    bullet=Bullet(player_x,PLAYER_Y,"Images\SI_bullet_test.jpg",10,30,screen,pygame.Rect(player_x,PLAYER_Y,20,60))
    bullet_list.append(bullet)
    return bullet

##game running
running = True
while running: 
    screen.fill([0,0,0])
    player_creation()

    ##rectangle creation
    player_rect=pygame.Rect(player_x+60, PLAYER_Y, 60, 45)
    test_player_rect=pygame.draw.rect(screen, colour, pygame.Rect(350, 450, 60, 60))
    test_bullet_rect=pygame.draw.rect(screen, colour, pygame.Rect(150, 150, 60, 60))

    ##bullet movement and boundry detection
    bullets_to_remove = []
    for bullet in bullet_list:
        bullet.bullet_move()
        if bullet.y <= -30:
            bullets_to_remove.append(bullet)

        # check collision between this bullet's rect and the test target
        if bullet.rect.colliderect(test_bullet_rect):
            print("Bullet collision detected")
            bullets_to_remove.append(bullet)
    
    ##player collision detection
    if player_rect.colliderect(test_player_rect):
        print("collision detected")
        player_lives-=1
        print(f"{player_lives} lives remaining")
        player_x=175
        player_rect.update(player_x+60, PLAYER_Y, 175, 50)
    if player_lives==0:
        print("Game Over")
        running=False
    
    ##user interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                player_x -= 5
                player_rect.update(player_x, PLAYER_Y, 175, 50)
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
                player_x += 5
                player_rect.update(player_x, PLAYER_Y, 175, 50)
            elif event.key == pygame.K_SPACE:
                print("Space key pressed")
                bullet = player_shoot()
                
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
    ##player boundry detection 
    if player_x<-60:
        player_x+=5
        player_rect.update(player_x, PLAYER_Y, 175, 50)
    elif player_x>385:
        player_x-=5
        player_rect.update(player_x, PLAYER_Y, 175, 50)
    
    ##bullet list removal
    for bullet in bullets_to_remove:
        if bullet in bullet_list:
            bullet_list.remove(bullet)
    
    

    pygame.display.flip()


pygame.quit()
pygame.display.quit()
