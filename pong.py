import pygame
import random

# Inicializa o pygame
pygame.init()

# Definindo as cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Definindo o tamanho da tela
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Definindo variáveis do jogo
paddle_width = 10
paddle_height = 60
ball_radius = 7
ball_speed_x = 5
ball_speed_y = 5
paddle_speed = 5

# Posições iniciais das raquetes e da bola
paddle1_y = height // 2 - paddle_height // 2
paddle2_y = height // 2 - paddle_height // 2
ball_x = width // 2
ball_y = height // 2

# Definindo o relógio
clock = pygame.time.Clock()

# Função para desenhar as raquetes e a bola
def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, white, [10, paddle1_y, paddle_width, paddle_height])
    pygame.draw.rect(screen, red, [width - 20, paddle2_y, paddle_width, paddle_height])  # Raquete da direita em vermelho
    pygame.draw.circle(screen, white, [ball_x, ball_y], ball_radius)
    pygame.display.flip()

# Função principal do jogo
def game_loop():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_speed_x, ball_speed_y

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Movimentação das raquetes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s] and paddle1_y < height - paddle_height:
            paddle1_y += paddle_speed
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
            paddle2_y += paddle_speed

        # Movimentação da bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisão com as paredes
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
            ball_speed_y *= -1

        # Colisão com as raquetes
        if (ball_x - ball_radius <= 20 and paddle1_y <= ball_y <= paddle1_y + paddle_height) or \
           (ball_x + ball_radius >= width - 20 and paddle2_y <= ball_y <= paddle2_y + paddle_height):
            ball_speed_x *= -1

        # Reinicia a bola se passar por uma raquete
        if ball_x < 0 or ball_x > width:
            ball_x = width // 2
            ball_y = height // 2
            ball_speed_x *= random.choice([1, -1])
            ball_speed_y *= random.choice([1, -1])

        # Desenha os objetos na tela
        draw_objects()

        # Define a taxa de quadros
        clock.tick(60)

    pygame.quit()
    quit()

# Inicia o jogo
game_loop()