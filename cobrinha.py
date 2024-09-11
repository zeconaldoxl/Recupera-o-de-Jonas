import pygame
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo cores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definindo tamanho da tela
width = 600
height = 400

# Criando a janela do jogo
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio
clock = pygame.time.Clock()

# Definindo o tamanho do bloco da cobra e a velocidade do jogo
snake_block = 10
snake_speed = 5

# Definindo fontes
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Função para exibir a pontuação
def show_score(score):
    value = score_font.render("Pontuação: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

# Função para desenhar a cobra
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, blue, [block[0], block[1], snake_block, snake_block])

# Função para exibir a mensagem final
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Função principal do jogo
def game_loop():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x = width / 2
    y = height / 2

    # Alterações de movimento
    dx = 0
    dy = 0

    # Lista para armazenar os blocos da cobra
    snake_list = []
    snake_length = 1

    # Posição da comida
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("Você perdeu! Pressione C para continuar ou Q para sair", red)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += dx
        y += dy
        screen.fill(black)

        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Iniciando o jogo
game_loop()