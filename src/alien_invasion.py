import sys

import pygame


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Inicializa o jogo e cria a janela."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Mantém a janela aberta até o usuário fechá-la."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()