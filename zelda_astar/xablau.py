import pygame

MONTANHA_COLOR = (139, 69, 19) # marrom
NEVE_COLOR = (0, 191, 255) # azul
AGUA_COLOR = (0, 255, 255) # ciano

colors = {
    "MONTANHA": MONTANHA_COLOR,
    "NEVE": NEVE_COLOR,
    "ÁGUA": AGUA_COLOR,
}

grid = [
    ["MONTANHA", "NEVE", "ÁGUA", "ÁGUA"],
    ["NEVE", "MONTANHA", "ÁGUA", "MONTANHA"],
    ["MONTANHA", "ÁGUA", "NEVE", "NEVE"],
    ["MONTANHA", "MONTANHA", "MONTANHA", "MONTANHA"], 
    ["MONTANHA", "MONTANHA", "MONTANHA", "MONTANHA"],
    ["MONTANHA", "MONTANHA", "MONTANHA", "MONTANHA"],
    ["MONTANHA", "MONTANHA", "MONTANHA", "MONTANHA"],
    ["MONTANHA", "MONTANHA", "MONTANHA", "MONTANHA"],
    ["MONTANHA", "MONTANHA", "MONTANHA", "MONTANHA"],
]

CELL_SIZE = 50

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*len(grid[0]), CELL_SIZE*len(grid)))
pygame.display.set_caption("Grid Example")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            color = colors[grid[i][j]]
            pygame.draw.rect(screen, color, (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()

pygame.quit()