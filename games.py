import pygame
from Player import Player
from Level import Level
from entities import Enemy, NPC, Item

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60  # Установка желаемой частоты кадров в секунду

# Определение параметров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# Создание объекта игрока
player = Player(x=400, y=300)  # Начальное положение игрока
# Создание объекта уровня
level = Level()  # Предполагается, что в конструкторе Level настраивается начальное состояние уровня

# Добавление игрока в группу спрайтов уровня
level.visible_sprites.add(player)

# Основной игровой цикл
running = True
while running:
    # Ограничение частоты кадров
    clock.tick(FPS)
    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление уровня и всех его спрайтов
    level.update(keys)  # Это должно включать обновление игрока

    # Отрисовка
    screen.fill((0, 0, 0))  # Заливка экрана черным цветом
    level.draw(screen)  # Это должно включать отрисовку игрока

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()