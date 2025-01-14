import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255, 255), self.position, self.radius)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        original_radius = self.radius
        original_velocity = self.velocity
        original_position = self.position
        self.kill()
        if ASTEROID_MIN_RADIUS >= original_radius:
            return
        split_rotation_base = random.uniform(20, 50)
        split_radius = original_radius - ASTEROID_MIN_RADIUS
        for i in range(ASTEROID_SPLIT_PIECES):
            split_asteroid = Asteroid(original_position.x, original_position.y, split_radius)
            split_rotation = (-1 ** i) * ((1+i)//2) * split_rotation_base
            split_asteroid.velocity = 1.2 * original_velocity.rotate(split_rotation)