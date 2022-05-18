from pydantic import BaseModel, Field
from models.general.TipoProducto import TipoProducto
from models.general.Genero import Genero


class Producto(BaseModel):
    id: int = Field(...)
    descripcion: str = Field(...)
    valor_compra: float = Field(...)
    valor_venta: float = Field(...)
    cantidad: int = Field(...)
    categoria: TipoProducto = Field(...)
    genero: Genero = Field(...)
