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
while running:
    pass # Здесь будет основной цикл Pygame

pygame.quit() # Чтобы закрыть Pygame