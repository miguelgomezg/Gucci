from dataclasses import dataclass

from models.BaseUbicacion import BaseUbicacion
from models.Moneda import Moneda


@dataclass
class Pais(BaseUbicacion):
    moneda: Moneda
    