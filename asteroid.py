import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        if self.radius == ASTEROID_MIN_RADIUS:
            pygame.draw.circle(screen, "green", self.position, self.radius, LINE_WIDTH)
        elif self.radius == ASTEROID_MAX_RADIUS:
            pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        else:
            pygame.draw.circle(screen, "blue", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            first_new_velocity = self.velocity.rotate(new_angle)
            second_new_velocity = self.velocity.rotate(0 - new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_new_asteroid.velocity = first_new_velocity * 1.2
            second_new_asteroid.velocity = second_new_velocity * 1.2
