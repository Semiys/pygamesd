import pygame
from Player import Player
from Level import Level
from entities import Enemy, NPC, Item

# Инициализация Pygame
pygame.init()

# Определение параметров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# Создание объекта игрока
player = Player(x=400, y=300)  # Начальное положение игрока

# Основной игровой цикл
running = True
while running:
    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление игрока
    player.update(keys)


    # Обновление игрового мира
    # ...

    # Отрисовка
    screen.fill((0, 0, 0))  # Заливка экрана черным цветом
    # ...
    # Отрисовка игрока
    player.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()