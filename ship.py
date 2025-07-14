import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:

    def __init__(self, game: "AlienInvasion", arsenal: "Arsenal"):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.image_90_degrees = pygame.transform.rotate(self.image, 90)
        self.image_270_degrees = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def update(self):
        # updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if (
            self.moving_right
            and self.rect.right < self.boundaries.right
            and self.rect.bottom == self.boundaries.bottom
        ):
            self.x += temp_speed
        if (
            self.moving_left
            and self.rect.left > self.boundaries.left
            and self.rect.bottom == self.boundaries.bottom
        ):
            self.x -= temp_speed
        if self.moving_up:
            if (
                self.rect.left == self.boundaries.left
                and self.rect.top > self.boundaries.top
            ):
                self.y -= temp_speed
            if (
                self.rect.right == self.boundaries.right
                and self.rect.top > self.boundaries.top
            ):
                self.y -= temp_speed
        if self.moving_down:
            if (
                self.rect.left == self.boundaries.left
                and self.rect.bottom < self.boundaries.bottom
            ):
                self.y += temp_speed
            if (
                self.rect.right == self.boundaries.right
                and self.rect.bottom < self.boundaries.bottom
            ):
                self.y += temp_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.arsenal.draw()
        if (
            self.rect.right == self.boundaries.right
            and self.rect.bottom < self.boundaries.bottom
        ):
            self.rect_90_derees = self.image_90_degrees.get_rect(
                center=self.rect.center
            )
            self.screen.blit(self.image_90_degrees, self.rect_90_derees)
            self.settings.arsenal_shoot_left = True
        elif (
            self.rect.left == self.boundaries.left
            and self.rect.bottom < self.boundaries.bottom
        ):
            self.screen.blit(self.image_270_degrees, self.rect)
            self.settings.arsenal_shoot_right = True
        else:
            self.screen.blit(self.image, self.rect)
            self.settings.arsenal_shoot_right = False
            self.settings.arsenal_shoot_left = False

    def fire(self):
        return self.arsenal.fire_bullet()
