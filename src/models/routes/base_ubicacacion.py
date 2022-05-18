from pydantic import BaseModel, Field


class BaseUbicacion(BaseModel):
    nombre: str = Field(...)
    codigo: int = Field(...)
