import pygame
#enemy class creation
class Enemy:
    def __init__(self,x,y,image,length,height):
        self.x=x
        self.y=y
        self.image=image
        self.length=length
        self.height=height
        self.move_right=True
        self.move_left=False

    ##enemy move function
    def move_enemies(self):
        if self.x>425:
            self.move_right=False
            self.move_left=True
            self.y+=10
        elif self.x<0:
            self.move_right=True
            self.move_left=False
            self.y+=10
        if self.move_right==True:
            self.x+=5
            pygame.time.wait(100) 
        elif self.move_left==True:
            self.x-=5
            pygame.time.wait(100) 
