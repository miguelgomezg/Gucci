from fastapi import APIRouter


from api.routes import user, product, invoce

router = APIRouter()
router.include_router(user.router, tags=["Usuarios"], prefix="/users")
router.include_router(product.router, tags=["Productos"], prefix="/products")
router.include_router(invoce.router, tags=["Facturas"], prefix="/invoce")
