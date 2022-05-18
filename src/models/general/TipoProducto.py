from enum import Enum


class TipoProducto(str, Enum):
    MEDIAS: str = "medias"
    GAFAS: str = "gafas"
    RELOJ: str = "reloj"
    GORRA: str = "gorra"
    BOLSO: str = "bolso"
    CAMISA: str = "camisa"
    PANTALON: str = "pantalon"
    ZAPATO: str = "zapato"
    INTERIOR: str = "interior"
