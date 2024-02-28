import pygame
import sys
from scoring import Score  # Importez Score depuis scoring.py

# Initialisation de quelques constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def over_screen(score):
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Game Over')

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    retry_button = pygame.Rect(300, 325, 200, 50)  # Coordonnées et dimensions du bouton "Réessayer"

    running = True
    retry_clicked = False  # Nouvelle variable pour suivre l'état du bouton "Réessayer" cliqué
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if retry_button.collidepoint(mouse_pos):
                    retry_clicked = True  # Mettre à jour l'état du bouton "Réessayer" cliqué

        screen.fill(WHITE)
        draw_text(screen, 'Game Over', font, BLACK, SCREEN_WIDTH // 2, 200)
        draw_text(screen, 'You Lost!', font, BLACK, SCREEN_WIDTH // 2, 250)

        pygame.draw.rect(screen, GRAY, retry_button)  # Dessiner le bouton "Réessayer" en gris
        draw_text(screen, 'Réessayer', font, BLACK, retry_button.centerx, retry_button.centery)

        # Afficher le score au centre de l'écran
        draw_text(screen, f'Score: {score.score_value}', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.update()
        clock.tick(30)

        if retry_clicked:  # Si le bouton "Réessayer" est cliqué, sortir de la boucle
            break

    return retry_clicked  # Retourner l'état du bouton "Réessayer" cliqué

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

if __name__ == "__main__":
    over_screen()
