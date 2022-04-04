from dataclasses import dataclass
from models.Ciudad import Ciudad
from models.Pais import Pais


@dataclass
class Ubicacion:
    pais: Pais
    ciudad: Ciudad
    direccion: str