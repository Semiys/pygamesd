# level.py
import pygame
from Player import Player  # Импортируем класс игрока
from obstacle import Obstacle  # Импортируем класс препятствия

class Level:
    def __init__(self):
        # Инициализация уровня
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.player = None  # Ссылка на игрока

    def setup_level(self, layout):
        # Создание уровня на основе предоставленного макета
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                if cell == 'X':
                    obstacle = Obstacle(x, y)
                    self.obstacles_sprites.add(obstacle)
                    self.visible_sprites.add(obstacle)
                elif cell == 'P':
                    self.player = Player(x, y)  # Создание и сохранение игрока
                    self.visible_sprites.add(self.player)

    def update(self, keys):
        # Обновление всех спрайтов
        self.visible_sprites.update(keys)

        # Обработка ввода пользователя, если игрок существует
        if self.player:
            self.player.update(keys)

    def draw(self, surface):
        # Отрисовка всех спрайтов
        self.visible_sprites.draw(surface)

# Пример использования класса Level
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    level = Level()

    # Пример макета уровня
    level_layout = [
        '............................',
        '............................',
        '............XXX.............',
        '............XXX.............',
        'P...........................',
    ]

    level.setup_level(level_layout)

    # Игровой цикл
    running = True
    while running:
        # Получение состояния клавиш
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление уровня
        level.update(keys)

        # Отрисовка уровня
        screen.fill((0, 0, 0))  # Заливка экрана черным цветом
        level.draw(screen)

        pygame.display.update()
        clock.tick(60)  # 60 FPS

    pygame.quit()