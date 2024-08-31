import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36
HANGMAN_PARTS_COLOR = (0, 0, 0)
HANGMAN_POSITION = (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 100)
WORDS = ["PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS"]

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hangman Game")

# Set up font
font = pygame.font.SysFont(None, FONT_SIZE)

# Hangman parts coordinates
HANGMAN_PARTS = [
    (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50), # base
    (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50), # post
    (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50),# beam
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

def get_random_word():
    return random.choice(WORDS)

def main():
    word = get_random_word()
    guessed_word = ["_"] * len(word)
    incorrect_guesses = 0
    max_incorrect_guesses = len(HANGMAN_PARTS)
    guessed_letters = set()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter in word:
                            for i, char in enumerate(word):
                                if char == letter:
                                    guessed_word[i] = letter
                        else:
                            incorrect_guesses += 1

        screen.fill(BACKGROUND_COLOR)
        
        draw_text("Hangman Game", font, FONT_COLOR, screen, WINDOW_WIDTH // 2, 50)
        draw_text(" ".join(guessed_word), font, FONT_COLOR, screen, WINDOW_WIDTH // 2, 150)
        draw_text("Incorrect guesses: " + str(incorrect_guesses), font, FONT_COLOR, screen, WINDOW_WIDTH // 2, 200)
        
        draw_hangman(incorrect_guesses)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
