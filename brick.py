import pygame

pygame.init

class Brick(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()