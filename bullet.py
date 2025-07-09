import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        self.image_90_degrees = pygame.transform.rotate(self.image, 90)
        self.shoot_left = self.settings.arsenal_shoot_left
        self.shoot_right = self.settings.arsenal_shoot_right
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        if self.shoot_left:
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x
        elif self.shoot_right:
            self.x += self.settings.bullet_speed
            self.rect.x = self.x
        else:
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y

    def draw_bullet(self):
        if self.shoot_left or self.shoot_right == True:
            self.screen.blit(self.image_90_degrees, self.rect)
        else:
           self.screen.blit(self.image, self.rect)