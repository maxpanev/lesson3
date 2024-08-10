import pygame
import random

pygame.init() # Чтобы запустить Pygame

SCREEN_WIDTH = 800 # Задаем переменные с размерами экрана
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Создаем экран


pygame.display.set_caption("Игра Тир") # Задаем заголовок окна
icon = pygame.image.load("img/42648.jpg") # Загружаем иконку приложения
pygame.display.set_icon(icon) # Устанавливаем иконку приложения

target_image = pygame.image.load("img/target.png") # Загружаем изображение цели
target_width, target_height = 80, 80 # Получаем размеры изображения цели

target_x = random.randint(0, SCREEN_WIDTH - target_width) # Случайное положение цели по горизонтали
target_y = random.randint(0, SCREEN_HEIGHT - target_height) # Случайное положение цели по вертикали

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



running = True
while running: # Здесь будет основной цикл Pygame
    screen.fill(color) # Закрашиваем экран в рандомный цвет
    for event in pygame.event.get(): # Проверяем события
        if event.type == pygame.QUIT: # Если нажата кнопка "Закрыть"
            running = False # Завершаем цикл
        if event.type == pygame.MOUSEBUTTONDOWN: # Если нажата кнопка мыши
            mouse_x, mouse_y = pygame.mouse.get_pos() # Получаем координаты курсора мыши
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= mouse_y + target_height: # Если курсор мыши попал в область цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y)) # Рисуем изображение цели на экране
    pygame.display.update() # Обновляем экран



pygame.quit() # Чтобы закрыть Pygame