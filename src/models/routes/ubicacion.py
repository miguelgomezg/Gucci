from pydantic import BaseModel, Field
from models.routes.pais import Pais
from models.routes.ciudad import Ciudad


class Ubicacion(BaseModel):
    pais: Pais = Field(...)
    ciudad: Ciudad = Field(...)
    direccion: str = Field(...)
