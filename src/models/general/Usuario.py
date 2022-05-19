from dataclasses import dataclass
from datetime import date
from models.general.TipoProducto import TipoProducto

from models.general.Ubicacion import Ubicacion


@dataclass
class Usuario:
    id: int
    email: str
    nombre: str
    apellido: str
    direccion: Ubicacion
    producto_interes: TipoProducto
    fecha_nacimiento: date
    password: str
