import sys
import pygame
from random import randint
from math import sin, cos, radians
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

#グローバル 設定
WIDTH = 600
HEIGHT = 600
INIT_SPEED = 10
BALL_SIZE = 20
BALL_COLOR = (180, 180, 180)
RACKET_SIZE = (300, 500, 80, 10)
RACKET_COLOR = (20, 100, 150)
ANGLE = 30

def main():
    pygame.init()
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Squash game")
    font = pygame.font.Font(None, 80)
    message_over = font.render("Game Over!!", True, (255, 0,0))
    message_pos = message_over.get_rect()
    message_pos.centerx = surface.get_rect().centerx
    message_pos.centery = surface.get_rect().centery

    ball_num = 3
    racket = Rect(RACKET_SIZE)
    ball = Rect(surface.get_rect().centerx - 10, 0, BALL_SIZE)
    dir = randint(ANGLE, 180 - ANGLE)
    speed = INIT_SPEED
    game_over = False

    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == KEYDOWN:
          if event.key == K_LEFT:
            racket.centerx -= 10
        elif event.key == K_RIGHT:
          racket.centerx += 10
        elif event.key == K_UP:
          racket.centery -= 10
        elif event.key == K_DOWN:
          racket.centery += 10

      # ボールの移動
      if ball.centery < HEIGHT:
        ball.centerx += cos(radians(dir)) * speed
        ball.centery += sin(radians(dir)) * speed
      else:
        if ball_num > 1:
          ball_num -= 1
          ball.left = surface.get_rect().centerx - 10
          ball.top = 0
          dir = randint(ANGLE, 180 - ANGLE)
        else:
          game_over = True
      if racket.collidedict(ball):
        dir = -(90 + (racket.centerx - ball.centerx) / racket.width * 100)
      if ball.centerx < 0 or ball.centerx > WIDTH:
        dir = 180 - dir
      dir = -dir if ball.centery < 0 else dir
      surface.fill((255, 255, 255))
      if game_over:
        surface.blit(message_over, (message_pos))
        pygame.draw.rect(surface, RACKET_COLOR, racket)
        pygame.draw.ellipse(surface, BALL_COLOR, ball)
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
  main()
