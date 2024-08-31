import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36
HANGMAN_PARTS_COLOR = (0, 0, 0)
HANGMAN_POSITION = (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 100)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Awesome hangman!!")
font = pygame.font.SysFont(None, FONT_SIZE)

HANGMAN_PARTS = [
    (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50), # base
    (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50), # post
    (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50), # cross
    (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 20), # the rope
    (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2), # head
    (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 20), # body
    (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 + 40), # left arm
    (WINDOW_WIDTH // 2 - 30, WINDOW_HEIGHT // 2 + 40), # right arm
    (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 + 70), # left leg
    (WINDOW_WIDTH // 2 - 30, WINDOW_HEIGHT // 2 + 70), # right leg
]

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_hangman(parts_drawn):
    for i in range(parts_drawn):
        pygame.draw.circle(screen, HANGMAN_PARTS_COLOR, HANGMAN_PARTS[i], 10)

def main():
    word = "PYTHON"#for now just one word
    guessed_word = ["_"] * len(word)
    incorrect_guesses = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        
        draw_text("Awesome hangman!!", font, FONT_COLOR, screen, WINDOW_WIDTH // 2, 50)
        draw_text(" ".join(guessed_word), font, FONT_COLOR, screen, WINDOW_WIDTH // 2, 150)
        draw_text("Incorrect guesses: " + str(incorrect_guesses), font, FONT_COLOR, screen, WINDOW_WIDTH // 2, 200)
        
        draw_hangman(incorrect_guesses)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
