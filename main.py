import pygame
import random
import time

pygame.init()  # Инициализация Pygame

SCREEN_WIDTH = 800  # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создание экрана

pygame.display.set_caption("Игра Тир")  # Заголовок окна
icon = pygame.image.load("img/42648.jpg")  # Загрузка иконки приложения
pygame.display.set_icon(icon)  # Установка иконки

target_image = pygame.image.load("img/target.png")  # Загрузка изображения цели
target_width, target_height = 80, 80  # Размеры изображения цели

target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Случайная позиция по X
target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # Случайная позиция по Y

# Начальная скорость движения мишени
target_speed_x = 0.14
target_speed_y = 0.14

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Случайный цвет фона

# Инициализация переменной счета
score = 0
max_score = 0

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Установка времени окончания игры через 30 секунд
start_time = time.time()
game_duration = 30  # Продолжительность игры в секундах

running = True
while running:  # Основной цикл Pygame
    screen.fill(color)  # Закрашиваем экран в случайный цвет

    # Проверяем, прошло ли 30 секунд
    elapsed_time = time.time() - start_time
    if elapsed_time > game_duration:
        if score > max_score:
            max_score = score
        # Отображение итогового счета и максимального рекорда
        screen.fill((0, 0, 0))  # Очистка экрана
        final_score_text = font.render("Ваш счет: " + str(score), True, (255, 255, 255))
        max_score_text = font.render("Максимальный рекорд: " + str(max_score), True, (255, 255, 255))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        screen.blit(max_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
        pygame.display.update()
        pygame.time.wait(5000)  # Пауза на 5 секунд
        score = 0  # Сброс текущего счета
        start_time = time.time()  # Перезапуск таймера

    for event in pygame.event.get():  # Проверка событий
        if event.type == pygame.QUIT:  # Если нажата кнопка "Закрыть"
            running = False  # Завершаем цикл
        if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Координаты курсора мыши
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:  # Если курсор попал в цель
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 10  # Увеличиваем счет на 10

        # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение с границами экрана и изменение направления
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображение текущего счета на экране
    score_text = font.render("Счет: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Вычисление и отображение оставшегося времени
    remaining_time = max(0, game_duration - int(elapsed_time))
    time_text = font.render("Время: " + str(remaining_time), True, (255, 255, 255))
    screen.blit(time_text, (10, 50))

    screen.blit(target_image, (target_x, target_y))  # Рисуем изображение цели
    pygame.display.update()  # Обновляем экран

pygame.quit()  # Закрытие Pygame