import pygame
pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode([500,500])
screen.fill([0,0,0])
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
        self.bullet_image = pygame.transform.scale(self.bullet_image, (20, 60))
    
    def bullet_move(self):
        for i in range(48):
            self.y-=10
            pygame.display.flip()
            screen.blit(self.bullet_image, (self.x+78,self.y-12))
            pygame.time.wait(10)
