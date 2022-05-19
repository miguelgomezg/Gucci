from pydantic import BaseModel, Field
from models.general.TipoProducto import TipoProducto
from models.general.Genero import Genero


class FiltroProducto(BaseModel):
    cantidad_stock: int = Field(None)
    categoria: TipoProducto = Field(None)
    genero: Genero = Field(None)
    precio_min: float = Field(None)
    precio_max: float = Field(None)
