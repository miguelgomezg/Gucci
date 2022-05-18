from dataclasses import dataclass
from models.general.Ciudad import Ciudad
from models.general.Pais import Pais


@dataclass
class Ubicacion:
    pais: Pais
    ciudad: Ciudad
    direccion: str