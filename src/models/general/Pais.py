from dataclasses import dataclass

from models.general.BaseUbicacion import BaseUbicacion
from models.general.Moneda import Moneda


@dataclass
class Pais(BaseUbicacion):
    moneda: Moneda
