import pygame

from src.game_events import GameEventHandler
from tests.doubles import StubShip


def test_seta_direita_move_nave_com_stub():
    ship = StubShip()  # stub no lugar da nave real
    handler = GameEventHandler(ship, bullet_manager=None)

    evento = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
    handler.handle_keydown(evento)

    assert ship.moving_right is True


def test_espaco_dispara_projetil_com_mock(mocker):
    ship = StubShip()
    mock_bullet_manager = mocker.Mock()  # mock do gerenciador de projéteis
    handler = GameEventHandler(ship, mock_bullet_manager)

    evento = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    handler.handle_keydown(evento)

    # o mock permite verificar a INTERAÇÃO: o disparo foi chamado uma única vez
    mock_bullet_manager.fire_bullet.assert_called_once()