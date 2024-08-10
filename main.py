import pygame
import random
import time

pygame.init()  # Чтобы запустить Pygame

SCREEN_WIDTH = 800  # Задаем переменные с размерами экрана
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создаем экран

pygame.display.set_caption("Игра Тир")  # Задаем заголовок окна
icon = pygame.image.load("img/42648.jpg")  # Загружаем иконку приложения
pygame.display.set_icon(icon)  # Устанавливаем иконку приложения

target_image = pygame.image.load("img/target.png")  # Загружаем изображение цели
target_width, target_height = 80, 80  # Получаем размеры изображения цели

target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Случайное положение цели по горизонтали
target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # Случайное положение цели по вертикали

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализация переменной счета
score = 0
max_score = 0

# Задаем шрифт для отображения счета
font = pygame.font.Font(None, 36)

# Устанавливаем время окончания игры через 30 секунд
start_time = time.time()
game_duration = 30  # продолжительность игры в секундах

running = True
while running:  # Основной цикл Pygame
    screen.fill(color)  # Закрашиваем экран в рандомный цвет

    # Проверяем, прошло ли 30 секунд
    if time.time() - start_time > game_duration:
        if score > max_score:
            max_score = score
        # Отображаем итоговый счет и максимальный рекорд
        screen.fill((0, 0, 0))  # Очистка экрана
        final_score_text = font.render("Ваш счет: " + str(score), True, (255, 255, 255))
        max_score_text = font.render("Максимальный рекорд: " + str(max_score), True, (255, 255, 255))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        screen.blit(max_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
        pygame.display.update()
        pygame.time.wait(5000)  # Пауза на 5 секунд
        score = 0  # Сброс текущего счета
        start_time = time.time()  # Перезапуск таймера

    for event in pygame.event.get():  # Проверяем события
        if event.type == pygame.QUIT:  # Если нажата кнопка "Закрыть"
            running = False  # Завершаем цикл
        if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем координаты курсора мыши
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:  # Если курсор мыши попал в область цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 10  # Увеличиваем счет на 10

        # Отображение текущего счета на экране
    score_text = font.render("Счет: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(target_image, (target_x, target_y))  # Рисуем изображение цели на экране
    pygame.display.update()  # Обновляем экран

pygame.quit()  # Чтобы закрыть Pygame