import pygame

pygame.init()

class Paddle(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill('black')
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()

    def move_left(self,pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self,pixels):
        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700