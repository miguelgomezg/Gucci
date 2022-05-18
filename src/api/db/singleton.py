from models.general.Usuario import Usuario
from models.general.Producto import Producto
from models.general.Factura import Factura
from models.general.Proveedor import Proveedor
from models.general.Ubicacion import Ubicacion
from models.general.Ciudad import Ciudad
from models.general.Pais import Pais
from models.general.Moneda import Moneda

from models.routes.usuario import CrearUsuario, ObtenerUsuarios, ValidarUsuario
from models.routes.producto import Producto as dtoProducto
from models.routes.factura import Factura as dtoFactura
from models.routes.proveedor import Proveedor as dtoProveedor


class Tienda:
    usuarios: list[Usuario] = []
    catalogo: list[Producto] = []
    facturas: list[Factura] = []
    proveedores: list[Proveedor] = []

    @classmethod
    def agregar_usuarios(cls, usuario: CrearUsuario):
        cls.usuarios.append(Usuario(
            email=usuario.email,
            nombre=usuario.nombre,
            apellido=usuario.apellidos,
            direccion=Ubicacion(
                ciudad=Ciudad(nombre=usuario.direccion.ciudad.nombre,
                              codigo=usuario.direccion.ciudad.codigo),
                pais=Pais(nombre=usuario.direccion.pais.nombre,
                          codigo=usuario.direccion.pais.codigo,
                          moneda=Moneda(nombre=usuario.direccion.pais.moneda.nombre, sigla=usuario.direccion.pais.moneda.sigla)),
                direccion=usuario.direccion.direccion
            ),
            producto_interes=usuario.producto_interes,
            fecha_nacimiento=usuario.fecha_nacimiento,
            password=usuario.password
        ))

    @classmethod
    def obtener_usuarios(cls):
        return [ObtenerUsuarios(apellidos=usuario.apellido, nombre=usuario.nombre)
                for usuario in cls.usuarios]

    @classmethod
    def validar_usuario(cls, usuario: ValidarUsuario):
        for usu in cls.usuarios:
            if usu.password == usuario.password and usu.email == usuario.email:
                return ObtenerUsuarios(nombre=usu.nombre, apellidos=usu.apellido)

    @classmethod
    def agregar_producto(cls, producto: dtoProducto):
        nuevo_producto: bool = True

        for pro in cls.catalogo:
            if pro.id == producto.id:
                pro.cantidad += producto.cantidad
                nuevo_producto = False

        if nuevo_producto:
            cls.catalogo.append(Producto(
                id=producto.id,
                descripcion=producto.descripcion,
                valor_compra=producto.valor_compra,
                valor_venta=producto.valor_venta,
                cantidad=producto.valor_venta,
                categoria=producto.categoria,
                genero=producto.genero
            ))

    @classmethod
    def obtener_productos(cls):
        return [producto for producto in cls.catalogo]
