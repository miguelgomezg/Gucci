from pydantic import BaseModel, Field


class Moneda(BaseModel):
    nombre: str = Field(...)
    sigla: str = Field(...)
