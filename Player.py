# player.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Загрузка изображения игрока
        self.image = pygame.image.load('person/3 Cyborg/Cyborg_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5  # Скорость перемещения игрока

    def update(self, keys):
        # Обработка ввода для перемещения игрока
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        # Дополнительные действия, например, прыжок или стрельба, могут быть добавлены здесь

    def draw(self, screen):
        # Отрисовка игрока на экране
        screen.blit(self.image, self.rect)