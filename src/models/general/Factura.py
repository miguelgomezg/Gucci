from dataclasses import dataclass


@dataclass
class Factura:
    id: int
    datos: dict[str]
    