import pygame

pygame.init() # Чтобы запустить Pygame

SCREEN_WIDTH = 800 # Задаем переменные с размерами экрана
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Создаем экран


pygame.display.set_caption("Игра Тир") # Задаем заголовок окна
icon = pygame.image.load("icon.png") # Загружаем иконку приложения


running = True
while running:
    pass # Здесь будет основной цикл Pygame

pygame.quit() # Чтобы закрыть Pygame