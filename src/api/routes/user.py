import imp
from fastapi import APIRouter, Body, Depends, HTTPException, Depends
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from models.routes.usuario import CrearUsuario, ObtenerUsuarios, ValidarUsuario
from api.utils.response import UJSONResponse
from api.db.singleton import Tienda

router = APIRouter()


class Usuarios:
    @router.get("/ObtenerUsuarios")
    def usuarios(tienda: Tienda = Depends(Tienda)):
        return UJSONResponse(
            message="Datos encontrados",
            status_code=HTTP_200_OK,
            data=tienda.__class__.obtener_usuarios()
        )

    @router.post("/CrearUsuario")
    def crear_usuario(usuario: CrearUsuario, tienda: Tienda = Depends(Tienda)):
        tienda.__class__.agregar_usuarios(usuario)

        return UJSONResponse(
            message="ok",
            status_code=HTTP_201_CREATED,
            data=usuario
        )

    @router.post("/ValidarUsuario")
    def validar_usuario(usuario: ValidarUsuario, tienda: Tienda = Depends(Tienda)):
        usuario_validado = tienda.__class__.validar_usuario(usuario)
        if usuario_validado:
            return UJSONResponse(
                message="Usuario validado correctamente",
                status_code=HTTP_200_OK,
                data=usuario_validado
            )

        return UJSONResponse(
            message="Usuario no encontrado",
            status_code=HTTP_401_UNAUTHORIZED
        )
