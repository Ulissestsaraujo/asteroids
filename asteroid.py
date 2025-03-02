from circleshape import CircleShape
from constants import *
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_ang = random.uniform(20,50)
        asteroid_one_ang = self.velocity.rotate(random_ang)
        asteroid_two_ang = self.velocity.rotate(-random_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_two = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_one.velocity = asteroid_one_ang * 1.2
        asteroid_two.velocity = asteroid_two_ang * 1.2

