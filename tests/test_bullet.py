import pygame

from src.bullet import Bullet
from src.settings import Settings
from src.ship import Ship


def test_bullet_sobe_na_tela():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)
    bullet = Bullet(screen, settings, ship)

    y_inicial = bullet.y

    # ação
    bullet.update()

    # verificação: o projétil deve subir (y diminui)
    assert bullet.y < y_inicial