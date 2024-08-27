# level.py
import pygame
TILE_SIZE = 64  # Размер плитки в пикселях
from obstacle import Obstacle  # Импортируем класс препятствия
class ParallaxBackground:
    def __init__(self, image_paths, speed, horizon_height):
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()
        self.horizon_height = horizon_height
        self.layers = [
            pygame.transform.scale(
                pygame.image.load(path).convert_alpha(),
                (self.screen_width, self.horizon_height)
            ) for path in image_paths
        ]
        self.speeds = speed
        self.positions = [0] * len(image_paths)

    def update(self, player_velocity):
        # Обновление позиции каждого слоя фона
        for i, speed in enumerate(self.speeds):
            self.positions[i] -= player_velocity * speed

    def draw(self, surface):
        # Отрисовка каждого слоя фона
        for position, layer in zip(self.positions, self.layers):
            # Повторение изображения, если оно заканчивается
            x = position % layer.get_width()
            surface.blit(layer, (x - layer.get_width(), 0))
            if x < surface.get_width():
                surface.blit(layer, (x, 0))
class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            original_image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f"Cannot load image: {image_path}")
            raise SystemExit(e)
        self.image = pygame.transform.scale(original_image, (64, 64))
        self.rect = self.image.get_rect(topleft=(x, y))

class Level:
    def __init__(self,player, tiles):
        # Инициализация уровня
        self.player = player
        self.tiles = tiles
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.visible_sprites.add(self.player)

        # Инициализация уровня
        self.horizon_height = 375  # Примерное значение, измените по своему усмотрению
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()
        self.background = ParallaxBackground(
            ['background/frees/city 1/1.png', 'background/frees/city 1/4.png'],
            [0.5, 1],
            self.horizon_height
        )
        # Инициализация атрибутов движения
        self.moving_right = False
        self.moving_left = False
        self.speed = 5  # Примерное значение скорости
        self.vertical_velocity = 0  # Примерное значение вертикальной скорости



    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()  # Группа для плиток, по которым может ходить игрок
        # Создание уровня на основе предоставленного макета
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if cell == 'X':
                    tile = Tile('background/tiles/Tiles.png', x, y)
                    self.visible_sprites.add(tile)
                    self.tiles.add(tile)  # Добавляем плитку в группу для столкновений
                elif cell == 'P':
                    # Перемещение игрока в начальную позицию, а не создание нового
                    self.player.rect.topleft = (x, y)
        # Добавление плиток земли
        for y in range(self.horizon_height, self.screen_height, 64):  # 64 - размер плитки
            for x in range(0, self.screen_width, 64):
                ground_tile = Tile('background/tiles/Tiles.png', x, y)
                self.visible_sprites.add(ground_tile)
    def update(self,keys):

        # Обновление игрока и фона
        self.player.update(keys)
        self.background.update(self.player.velocity.x)

        # Обработка столкновений
        self.handle_collisions()
    def handle_collisions(self):
        # Обработка горизонтальных столкновений
        for tile in self.tiles:
            if self.player.rect.colliderect(tile.rect):
                if self.player.velocity.x > 0:  # Moving right
                    self.player.rect.right = tile.rect.left
                elif self.player.velocity.x < 0:  # Moving left
                    self.player.rect.left = tile.rect.right

        # Обработка вертикальных столкновений
        for tile in self.tiles:
            if self.player.rect.colliderect(tile.rect):
                if self.player.velocity_y > 0:  # Falling
                    self.player.rect.bottom = tile.rect.top
                    self.player.velocity_y = 0
                    self.player.is_jumping = False
                    self.player.is_falling = False
                elif self.player.velocity_y < 0:  # Jumping
                    self.player.rect.top = tile.rect.bottom
                    self.player.velocity_y = 0






    def draw(self, surface):
        # Отрисовка фона
        self.background.draw(surface)


        # Отрисовка всех спрайтов
        self.visible_sprites.draw(surface)

