from dataclasses import dataclass
from models.Genero import Genero

from models.TipoProducto import TipoProducto


@dataclass
class Producto:
    id: int
    descripcion: str
    valor_compra: float
    valor_venta: float
    cantidad: int
    categoria: TipoProducto
    genero: Genero