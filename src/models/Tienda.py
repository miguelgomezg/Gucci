from dataclasses import dataclass
from models.Factura import Factura
from models.Producto import Producto
from models.Proveedor import Proveedor

from models.Usuario import Usuario


@dataclass
class Tienda:
    usuarios: list[Usuario]
    catalogo: list[Producto]
    facturas: list[Factura]
    proveedores: list[Proveedor]