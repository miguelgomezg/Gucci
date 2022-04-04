from dataclasses import dataclass
from datetime import date
import email
from models.TipoProducto import TipoProducto

from models.Ubicacion import Ubicacion


@dataclass
class Usuario:
    email: str
    nombre: str
    apellido: str
    direccion: Ubicacion
    producto_interes: TipoProducto
    fecha_nacimiento: date
    password: str