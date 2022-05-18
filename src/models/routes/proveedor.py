from pydantic import BaseModel, Field

from models.general.TipoProducto import TipoProducto


class Proveedor(BaseModel):
    id: int = Field(...)
    nombre: str = Field(...)
    email: str = Field(...)
    telefono: str = Field(...)
    producto: TipoProducto = Field(...)
