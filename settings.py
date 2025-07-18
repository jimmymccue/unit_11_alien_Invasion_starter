from pathlib import Path


class Settings:

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.ship_angle = 0
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "impactSound.mp3"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.arsenal_shoot_left = False
        self.arsenal_shoot_right = False

        self.alien_image = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.asteroid_image = Path.cwd() / "Assets" / "images" / "Asteroid Brown.png"
        self.alien_file = self.alien_image
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.fleet_difficulty_level = 1
