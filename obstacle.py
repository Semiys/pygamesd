# obstacle.py
import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Задайте размеры препятствия
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 0, 0))  # Заполнение красным цветом для наглядности
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # Метод update может содержать логику для анимации или движения препятствия
        pass