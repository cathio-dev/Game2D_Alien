from abc import ABC, abstractmethod


# ---------- ISP: várias interfaces pequenas e específicas ----------
class IDesconto(ABC):
    """Contrato mínimo de qualquer desconto."""

    @abstractmethod
    def calcular(self, valor: float) -> float:
        """Retorna o valor do desconto para o valor informado."""
        raise NotImplementedError


class ICupom(ABC):
    """Contrato para descontos que aceitam cupom."""

    @abstractmethod
    def aplicar_cupom(self, codigo: str) -> bool:
        raise NotImplementedError


class IVIP(ABC):
    """Contrato para descontos que validam usuário VIP."""

    @abstractmethod
    def validar_usuario_vip(self, usuario: str) -> bool:
        raise NotImplementedError


# ---------- LSP: qualquer filha substitui IDesconto sem quebrar ----------
class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor: float) -> float:
        return valor * 0.2

    def aplicar_cupom(self, codigo: str) -> bool:
        return True

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario == "vip"


class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3


def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    """Funciona com qualquer IDesconto (LSP)."""
    return desconto.calcular(valor)


def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)


# ---------- DIP: Pedido depende da abstração, não da implementação ----------
class Pedido:
    def __init__(self, desconto: IDesconto) -> None:
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)


def main() -> None:
    valor = 100

    print("Normal:", aplicar_desconto(DescontoNormal(), valor))
    print("VIP:", aplicar_desconto(DescontoVIP(), valor))
    print("Premium:", aplicar_desconto(DescontoPremium(), valor))
    print("Cupom VIP:", aplicar_cupom(DescontoVIP(), "DESC10"))

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())
    print("Pedido Normal:", pedido_normal.total(valor))
    print("Pedido VIP:", pedido_vip.total(valor))


if __name__ == "__main__":  # pragma: no cover
    main()