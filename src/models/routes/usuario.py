from datetime import datetime
from pydantic import BaseModel, Field

from models.general.TipoProducto import TipoProducto
from models.routes.ubicacion import Ubicacion


class CrearUsuario(BaseModel):
    email: str = Field(...)
    nombre: str = Field(...)
    apellidos: str = Field(...)
    direccion: Ubicacion = Field(...)
    producto_interes: TipoProducto = Field(...)
    fecha_nacimiento: datetime = Field(...)
    password: str = Field(...)


class ObtenerUsuarios(BaseModel):
    id: int = Field(...)
    nombre: str = Field(...)
    apellidos: str = Field(...)


class ValidarUsuario(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
