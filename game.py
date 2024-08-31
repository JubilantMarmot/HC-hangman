import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("my simple hangman")
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        draw_text("my simple hangman", font, FONT_COLOR, screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        pygame.display.flip()

if __name__ == "__main__":
    main()
