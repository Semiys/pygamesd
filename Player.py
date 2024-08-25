import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Загрузка изображений для анимации покоя
        self.idle_frames = [pygame.image.load(f'assets/perso/Cyborgsolo_idle{i}.png').convert_alpha() for i in range(1, 5)]
        self.run_frames = [pygame.image.load(f'assets/run/Cyborgsolo_run{i}.png').convert_alpha() for i in
                           range(1, 6)]
        self.jump_frame = [pygame.image.load(f'assets/jump/Cyborgsolo_jump{i}.png').convert_alpha() for i in
                           range(1, 5)]
        self.current_frame = 0
        self.image = self.idle_frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
        self.last_updated_time = pygame.time.get_ticks()
        self.animation_speed = 220  # скорость анимации в миллисекундах
        # Состояния игрока
        self.is_jumping = False
        self.is_running = False
        self.is_falling = False
        self.jump_speed = -10  # начальная скорость прыжка
        self.gravity = 0.5  # гравитация
        self.velocity_y = 0  # текущая вертикальная скорость
        self.ground_level = 350  # Уровень "невидимой земли"
        self.direction = 1  # 1 - право, -1 - лево
        self.image_flipped = False

    def flip_image(self):
        if self.direction == -1 and not self.image_flipped:
            self.idle_frames = [pygame.transform.flip(img, True, False) for img in self.idle_frames]
            self.run_frames = [pygame.transform.flip(img, True, False) for img in self.run_frames]
            self.jump_frame = [pygame.transform.flip(img, True, False) for img in self.jump_frame]
            self.image_flipped = True
            self.current_frame = 0  # Сброс текущего кадра
        elif self.direction == 1 and self.image_flipped:
            self.idle_frames = [pygame.transform.flip(img, True, False) for img in self.idle_frames]
            self.run_frames = [pygame.transform.flip(img, True, False) for img in self.run_frames]
            self.jump_frame = [pygame.transform.flip(img, True, False) for img in self.jump_frame]
            self.image_flipped = False
            self.current_frame = 0  # Сброс текущего кадра
    def animate_idle(self):
        # Обновление изображения игрока для анимации покоя
        now = pygame.time.get_ticks()
        if now - self.last_updated_time > self.animation_speed:
            self.last_updated_time = now
            self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
            self.image = self.idle_frames[self.current_frame]


    def animate_run(self):
        # Обновление изображения игрока для анимации бега
        now = pygame.time.get_ticks()
        if now - self.last_updated_time > self.animation_speed:
            self.last_updated_time = now
            self.current_frame = (self.current_frame + 1) % len(self.run_frames)
            self.image = self.run_frames[self.current_frame]



    def start_jump(self):
        if not self.is_jumping and not self.is_falling:
            self.is_jumping = True
            self.velocity_y = self.jump_speed

    def animate_jump(self):
        # Переключение кадров анимации прыжка в зависимости от вертикальной скорости
        if self.velocity_y < -10:  # Большая скорость вверх
            self.image = self.jump_frame[0]
        elif self.velocity_y < -5:  # Средняя скорость вверх
            self.image = self.jump_frame[1]
        elif self.velocity_y < 0:  # Малая скорость вверх
            self.image = self.jump_frame[2]
        elif self.velocity_y >= 0:  # Падение
            self.image = self.jump_frame[3]



    def update(self, keys):

        # Обработка ввода для перемещения игрока
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.is_running = True
            if self.direction != -1:  # Обновляем направление только если оно изменилось
                self.direction = -1
                self.flip_image()  # Вызов функции отражения изображения

        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.is_running = True
            if self.direction != 1:  # Обновляем направление только если оно изменилось
                self.direction = 1
                self.flip_image()  # Вызов функции отражения изображения

        else:
            self.is_running = False  # Сброс состояния бега, если нет движения
        # Прыжок
        if keys[pygame.K_SPACE] and not self.is_jumping and not self.is_falling:
            self.start_jump()

        # Обновление вертикального положения игрока
        if self.is_jumping or self.is_falling:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            self.is_running = False

            # Проверка на приземление (это просто пример, вам нужно будет настроить это)
            if self.rect.bottom >= self.ground_level:  # Используем переменную ground_level
                self.rect.bottom = self.ground_level
                self.is_jumping = False
                self.is_falling = False
                self.velocity_y = 0
            else:
                self.is_falling = True

        # Анимация игрока в зависимости от состояния
        if self.is_jumping or self.is_falling:
            self.animate_jump()
        elif self.is_running:
            self.animate_run()
        else:
            self.animate_idle()




    def draw(self, screen):
        # Отрисовка игрока на экране
        screen.blit(self.image, self.rect)