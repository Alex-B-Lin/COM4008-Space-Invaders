import pygame
pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode([500,500])
screen.fill([0,0,0])
##Bullet class
class Bullet:
    def __init__(self, x, y, bullet_image, length, height, screen, rect=None):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.screen = screen

        self.bullet_image = pygame.image.load(bullet_image)
        self.bullet_image = pygame.transform.scale(self.bullet_image, (self.length, self.height))
        self.rect = pygame.Rect(self.x + 83, self.y, self.length, self.height)

    def bullet_move(self):
        self.y -= 0.3
        self.rect.topleft = (self.x + 83, self.y)
        self.screen.blit(self.bullet_image, (self.x + 83, self.y))