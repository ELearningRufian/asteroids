import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    containers = []

    def __init__(self, x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_rate_limiter = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if 0 < self.shoot_rate_limiter:
            return
        shot_position = self.position + self.radius * pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(shot_position.x, shot_position.y)
        shot.velocity = PLAYER_SHOOT_SPEED * pygame.Vector2(0, 1).rotate(self.rotation)
        self.shoot_rate_limiter = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.shoot_rate_limiter -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()