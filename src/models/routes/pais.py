from pydantic import Field
from models.routes.moneda import Moneda
from models.routes.base_ubicacacion import BaseUbicacion


class Pais(BaseUbicacion):
    moneda: Moneda = Field(...)
