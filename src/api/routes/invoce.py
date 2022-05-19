from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from api.db.singleton import Tienda
from api.utils.response import UJSONResponse

router = APIRouter()


class Factura:
    @router.get("/ObtenerFacturas")
    def obtener_facturas(tienda: Tienda = Depends(Tienda)):
        return UJSONResponse(
            message="Facturas encontradas",
            data=tienda.__class__.obtener_facturas(),
            status_code=HTTP_200_OK
        )
