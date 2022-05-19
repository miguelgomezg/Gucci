from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from models.routes.producto import Producto
from api.utils.response import UJSONResponse
from api.db.singleton import Tienda

router = APIRouter()


class Productos:
    @router.post("/AgregarNuevoProducto")
    def agregar_nuevo_producto(producto: Producto, tienda: Tienda = Depends(Tienda)):
        tienda.__class__.agregar_producto(producto)

        return UJSONResponse(
            message="Producto agregado correctamente",
            status_code=HTTP_201_CREATED
        )

    @router.get("/ObtenerProductos")
    def obtener_productos(tienda: Tienda = Depends(Tienda)):
        return UJSONResponse(
            message="Productos encontrados",
            status_code=HTTP_200_OK,
            data=tienda.__class__.obtener_productos()
        )

    @router.get("/ObtenerProducto/{id}")
    def obtener_producto(id: int, tienda: Tienda = Depends(Tienda)):
        try:
            producto_encontrado = tienda.__class__.obtener_producto(id)
            if producto_encontrado:
                return UJSONResponse(
                    data=producto_encontrado,
                    message="Producto encontrado",
                    status_code=HTTP_200_OK
                )
            return UJSONResponse(
                message="El producto no fue encontrado",
                status_code=HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return UJSONResponse(
                message=e,
                status_code=HTTP_400_BAD_REQUEST
            )

    @router.put("/AumentarStock")
    def aumentar_stock(producto: Producto, tienda: Tienda = Depends(Tienda)):

        tienda.__class__.agregar_producto(producto)

        return UJSONResponse(
            message="Inventario modificado",
            status_code=HTTP_200_OK,
            data=producto
        )

    @router.post("/vender")
    def generar_venta(producto: Producto, tienda: Tienda = Depends(Tienda)):
        factura = tienda.__class__.vender_producto(producto)
        if factura:
            return UJSONResponse(
                message="Venta exitosa",
                status_code=HTTP_200_OK,
                data=factura
            )

        return UJSONResponse(
            message="Venta no exitosa",
            status_code=HTTP_400_BAD_REQUEST
        )
