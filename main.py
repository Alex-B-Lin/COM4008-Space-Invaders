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

##enemy class creation
#class Enemy:
#    def __init__(self,x,y,image,length,height):
#        self.x=x
#        self.y=y
#        self.image=image
#        self.length=length
#        self.height=height
#        self.move_right=True
#        self.move_left=False
#    
#    ##enemy move function
#    def move_enemies(self):
#        if self.x>425:
#            self.move_right=False
#            self.move_left=True
#            self.y+=10
#        elif self.x<0:
#            self.move_right=True
#            self.move_left=False
#            self.y+=10
#        if self.move_right==True:
#            self.x+=5
#            pygame.time.wait(100) 
#        elif self.move_left==True:
#            self.x-=5
#            pygame.time.wait(100) 





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


##Bullet class
class Bullet:
    def __init__(self,x,y,bullet_image,length,height,screen):
        self.x=x
        self.y=y
        self.bullet_image=bullet_image
        self.length=length
        self.height=height
        self.screen=screen

        self.bullet_image=pygame.image.load(bullet_image)
        self.bullet_image = pygame.transform.scale(self.bullet_image, (30, 30))
        self.screen.blit(self.bullet_image, (player_x+73, 430))
    def bullet_move(self,):
        
        while self.y>0:
            self.y-=10
            print("bullet move")



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
            elif event.key == pygame.K_SPACE:
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


