from pydantic import BaseModel, Field


class Factura(BaseModel):
    id: int = Field(...)
    datos: dict = Field(...)
