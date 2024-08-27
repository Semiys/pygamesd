import pygame
from player import Player
from level import Level

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
player = Player(x=100, y=100)  # Начальное положение игрока
tiles = [pygame.sprite.Sprite() for _ in range(5)]
for i, tile in enumerate(tiles):
    tile.image = pygame.Surface((100, 20))
    tile.image.fill((0, 255, 0))
    tile.rect = tile.image.get_rect(topleft=(i * 150, 400))

# Создание объекта уровня
level = Level(player, tiles)  # Предполагается, что в конструкторе Level настраивается начальное состояние уровня

# Добавление игрока в группу спрайтов уровня
level.visible_sprites.add(player)
level_layout = [
        '............................',
        '............................',
        '............XXX.............',
        '...X........XXX.............',
        '..XXX.......................',
        'P...........................',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',

    ]
level.setup_level(level_layout)
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
    keys = pygame.key.get_pressed()
    level.update(keys)  # Это должно включать обновление игрока

    # Отрисовка
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect.topleft)
    for tile in tiles:
        screen.blit(tile.image, tile.rect.topleft)
    # Заливка экрана черным цветом
    level.draw(screen)  # Это должно включать отрисовку игрока

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
