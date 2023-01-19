import pygame

disp = pygame.display.set_mode((800, 800))
pygame.display.set_caption("brick breaker")
FPS = 60


def draw(win):
    win.fill("white")
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    draw(disp)
    pygame.quit()
    quit()
