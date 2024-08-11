import pygame
import random
import time
import requests
from io import BytesIO

pygame.init() # Инициализация Pygame

SCREEN_WIDTH = 800 # Ширина экрана
SCREEN_HEIGHT = 600 # Высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Создание экрана

pygame.display.set_caption('Игра "Вражеские дроны"') # Заголовок окна
icon = pygame.image.load("img/42648.jpg") # Загрузка иконки приложения
pygame.display.set_icon(icon) # Установка иконки

target_image = pygame.image.load("img/enemy.png") # Загрузка изображения цели
target_width, target_height = 80, 80 # Размеры изображения цели

# Загрузка фона из интернета
background_url = "https://cq.ru/img/f/e/2023/11/08/42648.jpg"  # Укажите URL-адрес вашего изображения
response = requests.get(background_url)
background_image = pygame.image.load(BytesIO(response.content))

# Загрузка изображения курсора
cursor_image = pygame.image.load("img/cursor.png")  # Укажите путь к изображению курсора
cursor_image = pygame.transform.scale(cursor_image, (60, 50))  # Масштабирование изображения курсора

# Преобразование изображения в формат курсора Pygame
cursor_data = pygame.cursors.Cursor((0, 0), cursor_image)

# Установка собственного курсора
pygame.mouse.set_visible(False)  # Скрытие стандартного курсора
pygame.mouse.set_cursor(cursor_data)

# Инициализация переменной счета
score = 0
max_score = 0

font = pygame.font.Font(None, 36) # Шрифт для отображения текста

start_time = time.time() # Установка времени окончания игры
game_duration = 30 # Продолжительность игры в секундах

# Функция для создания мишеней
def create_targets():
    targets = []
    num_targets = random.randint(1, 4)
    for _ in range(num_targets):
        target_x = random.randint(0, SCREEN_WIDTH - target_width) # Случайная позиция по X
        target_y = random.randint(0, SCREEN_HEIGHT - target_height) # Случайная позиция по Y
        target_speed_x = random.choice([-1, 1]) * 0.14  # Движение мишени
        target_speed_y = random.choice([-1, 1]) * 0.14
        targets.append({"x": target_x, "y": target_y, "speed_x": target_speed_x, "speed_y": target_speed_y})
    return targets

targets = create_targets()

running = True
while running:
    screen.blit(background_image, (0, 0))
    # Проверяем, прошло ли 30 секунд
    elapsed_time = time.time() - start_time
    if elapsed_time > game_duration:
        if score > max_score:
            max_score = score # Отображение итогового счета и максимального рекорда
        screen.fill((0, 0, 0)) # Очистка экрана
        final_score_text = font.render("Ваш счет: " + str(score), True, (255, 255, 255))
        max_score_text = font.render("Максимальный рекорд: " + str(max_score), True, (255, 255, 255))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        screen.blit(max_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
        pygame.display.update()
        pygame.time.wait(5000) # Пауза на 5 секунд
        score = 0 # Сброс текущего счета
        start_time = time.time() # Перезапуск таймера
        targets = create_targets()

    for event in pygame.event.get(): # Проверка событий
        if event.type == pygame.QUIT: # Если нажата кнопка "Закрыть"
            running = False # Завершаем цикл
        if event.type == pygame.MOUSEBUTTONDOWN: # Если нажата кнопка мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Координаты курсора мыши
            for target in targets[:]:  # Создаём копию списка для безопасного удаления
                if target["x"] <= mouse_x <= target["x"] + target_width and target["y"] <= mouse_y <= target["y"] + target_height:  # Если курсор попал в цель
                    targets.remove(target)
                    score += 10
    for target in targets:
        target["x"] += target["speed_x"]
        target["y"] += target["speed_y"]

        if target["x"] <= 0 or target["x"] >= SCREEN_WIDTH - target_width:
            target["speed_x"] = -target["speed_x"]
        if target["y"] <= 0 or target["y"] >= SCREEN_HEIGHT - target_height:
            target["speed_y"] = -target["speed_y"]

        screen.blit(target_image, (target["x"], target["y"]))

    if len(targets) == 0:
        targets = create_targets()

    score_text = font.render("Счет: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Вычисление и отображение оставшегося времени
    remaining_time = max(0, game_duration - int(elapsed_time))
    time_text = font.render("Время: " + str(remaining_time), True, (255, 255, 255))
    screen.blit(time_text, (10, 50))

    # Отображение пользовательского курсора
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_image, (mouse_x, mouse_y))  # Отображение курсора на позиции мыши

    pygame.display.update()

pygame.quit()  # Закрытие Pygame