from alien import Alien


class FastAlien(Alien):
    """Alienígena mais rápido."""

    def update(self) -> None:
        """Move o alienígena com o dobro da velocidade."""
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = int(self.x)