import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Alien(Sprite):
    def __init__(self, fleet: "AlienInvasion", x: float, y: float):
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )
        self.image_90_degrees = pygame.transform.rotate(self.image, 90)
        self.shoot_left = self.settings.arsenal_shoot_left
        self.shoot_right = self.settings.arsenal_shoot_right

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        return (
            self.rect.right >= self.boundaries.right
            or self.rect.left <= self.boundaries.left
        )

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
