from src.desconto import IDesconto


class StubSemDesconto(IDesconto):
    """Stub: simula um desconto retornando sempre uma resposta controlada (0)."""

    def calcular(self, valor):
        return 0


class StubShip:
    """Stub da nave: tem apenas os atributos que o tratador de eventos usa."""

    def __init__(self):
        self.moving_right = False
        self.moving_left = False