import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
    	pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        keys = pygame.key.get_pressed()

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_vector = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.vector = self.velocity.rotate(new_vector)
            asteroid1.velocity = asteroid1.vector * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.vector = self.velocity.rotate(-new_vector)
            asteroid2.velocity = asteroid2.vector * 1.2
