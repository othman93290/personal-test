import pygame
import sys

# Définir quelques constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def presentation_screen():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    start_button = pygame.Rect(300, 300, 200, 50)
    start_text = font.render('Start', True, BLACK)

    running = True
    start_game = False  # Variable de contrôle pour démarrer le jeu
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    start_game = True  # Le joueur a cliqué sur le bouton "Start"
                    running = False

        screen.fill(WHITE)
        pygame.draw.rect(screen, (150, 150, 150), start_button)
        screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2, 
                                 start_button.y + (start_button.height - start_text.get_height()) // 2))  # Déplacer le texte au centre du bouton

        draw_text(screen, 'ptit snake 3310', font, BLACK, 330, 200)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

    print("start_game value:", start_game)  # Ajout d'un message de débogage
    return start_game, screen  # Renvoie True si le jeu doit être démarré, False sinon
