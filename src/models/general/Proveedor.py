from dataclasses import dataclass

from models.general.TipoProducto import TipoProducto


@dataclass
class Proveedor:
    id: int
    nombre: str
    email: str
    telefono: str
    producto: TipoProducto
