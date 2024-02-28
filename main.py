import pygame
from snake import Snake
from fruit import Fruit
from presentation import presentation_screen
from scoring import Score

# Importez over_screen depuis over.py ici
from over import over_screen

# Initialisation de quelques constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
FONT_PATH = pygame.font.match_font('arial')

def start_game(screen):
    print("Starting game...")  # Ajout d'un message de débogage

    pygame.init()  # Initialisation de Pygame

    # Initialisation du jeu
    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
    fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
    score = Score(FONT_PATH)  # Correction : passer seulement le chemin du fichier de police

    # Création de la surface d'affichage
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('ptit snake te3 3310')

    # Boucle principale du jeu
    clock = pygame.time.Clock()
    running = True
    game_over = False  # Variable pour détecter si le joueur a perdu
    while running:
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.turn((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.turn((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.turn((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.turn((1, 0))

            screen.fill(WHITE)
            snake.move()

            # Si le serpent mange le fruit
            if snake.get_head_position() == fruit.position:
                snake.length += 1
                fruit.randomize_position()
                score.increase_score()  # Augmenter le score lorsque le serpent mange le fruit
                print("Score:", score.score_value)  # Ajout d'un message de débogage pour vérifier le score

            # Vérifier si le serpent se touche lui-même
            if snake.head_collides_with_body():
                game_over = True

            snake.draw(screen)
            fruit.draw(screen)
            score.draw(screen)  # Afficher le score
            print("Drawing score...")  # Ajout d'un message de débogage pour vérifier si le score est dessiné
            pygame.display.update()
            clock.tick(10)  # Vitesse du jeu (10 frames par seconde)

        # Une fois la boucle de jeu terminée, afficher l'écran de fin de jeu
        if over_screen(score):  # Si la fonction over_screen() retourne True
            # Réinitialiser les valeurs du jeu
            snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
            fruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
            score = Score(FONT_PATH)
            game_over = False  # Réinitialiser la variable game_over

    pygame.quit()  # Assurez-vous que pygame.quit() est appelé après la bou

def main():
    pygame.init()

    should_start_game, screen = presentation_screen()

    if should_start_game:
        while True:  # Boucle pour relancer le jeu
            start_game(screen)
            if not over_screen(Score):  # Si over_screen() retourne False, arrêtez la boucle
                break

if __name__ == "__main__":
    main()
