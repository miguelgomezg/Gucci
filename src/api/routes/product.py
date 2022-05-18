import imp
from fastapi import APIRouter, Body, Depends, HTTPException, Depends
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from models.routes.producto import Producto
from api.utils.response import UJSONResponse
from api.db.singleton import Tienda

router = APIRouter()


class Productos:
    @router.post("/AgregarProductos")
    def agregar_producto(producto: Producto, tienda: Tienda = Depends(Tienda)):
        tienda.agregar_producto(producto)

        return UJSONResponse(
            message="Producto agregado correctamente",
            status_code=HTTP_201_CREATED
        )

    @router.get("/ObtenerProductos")
    def obtener_producto(tienda: Tienda = Depends(Tienda)):
        return UJSONResponse(
            message="Productos encontrados",
            status_code=HTTP_200_OK,
            data=tienda.obtener_productos()
        )
