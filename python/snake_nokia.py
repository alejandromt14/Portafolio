import pygame
import random
import sys

pygame.init()

CELL = 20
COLS = 15
ROWS = 15
WIDTH = CELL * COLS
HEIGHT = CELL * ROWS
INFO_H = 40

GREEN_DARK = (15, 56, 15)
GREEN_MID = (48, 98, 48)
GREEN_LIGHT = (139, 172, 15)
BG = (192, 192, 192)

screen = pygame.display.set_mode((WIDTH, HEIGHT + INFO_H))
pygame.display.set_caption("Serpiente Nokia")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 20, bold=True)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [(7, 7), (6, 7), (5, 7)]
        self.dir = (1, 0)
        self.next_dir = (1, 0)
        self.grow = False

    def set_dir(self, d):
        if (d[0] * -1, d[1] * -1) != self.dir:
            self.next_dir = d

    def update(self):
        self.dir = self.next_dir
        hx, hy = self.body[0]
        nx, ny = hx + self.dir[0], hy + self.dir[1]

        if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS:
            return False
        if (nx, ny) in self.body:
            return False

        self.body.insert(0, (nx, ny))
        if not self.grow:
            self.body.pop()
        self.grow = False
        return True

    def draw(self, surf):
        for seg in self.body:
            r = pygame.Rect(seg[0] * CELL, seg[1] * CELL, CELL, CELL)
            pygame.draw.rect(surf, GREEN_DARK, r)
            inner = r.inflate(-4, -4)
            pygame.draw.rect(surf, GREEN_MID, inner)


class Food:
    def __init__(self):
        self.pos = (0, 0)

    def spawn(self, snake_body):
        while True:
            p = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if p not in snake_body:
                self.pos = p
                return

    def draw(self, surf):
        cx = self.pos[0] * CELL + CELL // 2
        cy = self.pos[1] * CELL + CELL // 2
        pygame.draw.circle(surf, GREEN_DARK, (cx, cy), CELL // 2 - 2)


snake = Snake()
food = Food()
food.spawn(snake.body)
score = 0
game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_over:
                snake.reset()
                food.spawn(snake.body)
                score = 0
                game_over = False
            elif not game_over:
                if event.key == pygame.K_UP:
                    snake.set_dir((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.set_dir((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.set_dir((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.set_dir((1, 0))

    if not game_over:
        if not snake.update():
            game_over = True
        elif snake.body[0] == food.pos:
            snake.grow = True
            score += 1
            food.spawn(snake.body)

    screen.fill(BG)

    game_surf = pygame.Surface((WIDTH, HEIGHT))
    game_surf.fill(GREEN_LIGHT)
    snake.draw(game_surf)
    food.draw(game_surf)
    screen.blit(game_surf, (0, 0))

    pygame.draw.rect(screen, (100, 100, 100), (0, HEIGHT, WIDTH, INFO_H))
    txt = f"Puntos: {score}" if not game_over else f"GAME OVER! ENTER"
    txt_surf = font.render(txt, True, GREEN_DARK)
    screen.blit(txt_surf, (10, HEIGHT + 8))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
