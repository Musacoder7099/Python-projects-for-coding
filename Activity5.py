import pygame
import random
Screen_width,Screen_height = 500,400
Movement_Speed = 5
Font_size = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bg.jpeg"),(Screen_width,Screen_height))

font_text = pygame.font.SysFont("Times New Roman",Font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
      super().__init__()
      self.image = pygame.Surface([width,height])
      self.image.fill(
      pygame.colour('dodgerblue')
      pygame.draw.rect(self.image,colour,pygame.Rect(0,0,width,height))
      self.rect =self.image.get_rect()
    )
def move(self,x_change,y_change):
 self.rect.x = max
    min(self.rect.x + x_change , Screen_width - self.rect.width),0)
 self.rect.y = max
    min(self.rect.y + y_change , Screen_height - self.rect.height),0)