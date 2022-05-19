from datetime import datetime
from math import prod
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
from models.routes.filtro import FiltroProducto


class Tienda:
    usuarios: list[Usuario] = []
    catalogo: list[Producto] = []
    facturas: list[Factura] = []
    proveedores: list[Proveedor] = []

    ID_USUARIO: int = 1
    ID_PRODUCTO: int = 1
    ID_FACTURA: int = 1
    ID_PROVEEDOR: int = 1

# Usuarios
    @classmethod
    def agregar_usuarios(cls, usuario: CrearUsuario):
        cls.usuarios.append(Usuario(
            id=cls.ID_USUARIO,
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
        cls.ID_USUARIO += 1

    @classmethod
    def obtener_usuarios(cls):
        return [ObtenerUsuarios(id=usuario.id, apellidos=usuario.apellido, nombre=usuario.nombre)
                for usuario in cls.usuarios]

    @classmethod
    def validar_usuario(cls, usuario: ValidarUsuario):
        for usu in cls.usuarios:
            if usu.password == usuario.password and usu.email == usuario.email:
                return ObtenerUsuarios(nombre=usu.nombre, apellidos=usu.apellido)

    @classmethod
    def validar_descuento_nacimiento(cls, id: int):
        descuento_nacimiento = False

        for usu in cls.usuarios:
            if usu.id == id:
                descuento_nacimiento = usu.fecha_nacimiento == datetime.now().date()

        return descuento_nacimiento

# Catalogos

    @classmethod
    def agregar_producto(cls, producto: dtoProducto):
        nuevo_producto: bool = True

        for pro in cls.catalogo:
            if pro.id == producto.id:
                pro.cantidad = producto.cantidad
                nuevo_producto = False

        if nuevo_producto:
            cls.catalogo.append(Producto(
                id=cls.ID_PRODUCTO,
                descripcion=producto.descripcion,
                valor_compra=producto.valor_compra,
                valor_venta=producto.valor_venta,
                cantidad=producto.valor_venta,
                categoria=producto.categoria,
                genero=producto.genero
            ))
            cls.ID_PRODUCTO += 1

    @classmethod
    def obtener_productos(cls):
        return [producto for producto in cls.catalogo]

    @classmethod
    def obtener_producto(cls, id: int):
        for pro in cls.catalogo:
            if pro.id == id:
                return pro

    @classmethod
    def filtrar_productos(cls, filtro: FiltroProducto):
        pro_filtrados: list[Producto] = []

        for producto in cls.catalogo:
            if filtro.cantidad_stock:
                if producto.cantidad >= filtro.cantidad_stock:
                    pro_filtrados.append(producto)

            if filtro.categoria:
                if filtro.categoria == producto.categoria:
                    pro_filtrados.append(producto)

            if filtro.genero:
                if filtro.genero == producto.genero:
                    pro_filtrados.append(producto)

            if filtro.precio_min:
                if filtro.precio_min >= producto.valor_compra:
                    pro_filtrados.append(producto)

            if filtro.precio_max:
                if filtro.precio_max <= producto.valor_compra:
                    pro_filtrados.append(producto)

        return pro_filtrados

    @classmethod
    def validar_disponibilidad(cls, producto: dtoProducto):
        confirma_stock: bool = False

        for pro in cls.catalogo:
            if pro.id == producto.id and pro.cantidad <= producto.cantidad:
                confirma_stock = True

        return confirma_stock

    @classmethod
    def validar_descuento_cantidad(cls, producto: dtoProducto):
        return True if producto.cantidad > 12 else False

    @classmethod
    def vender_producto(cls, producto: dtoProducto):
        validar_disponibilidad = cls.validar_disponibilidad(producto)

        if validar_disponibilidad:
            for pro in cls.catalogo:
                if pro.id == producto.id:
                    pro.cantidad -= producto.cantidad
                    return cls.generar_factura(producto)

# Proveedores

    @classmethod
    def agregar_proveedor(cls, proveedor: dtoProveedor):
        cls.proveedores.append(proveedor)

    @classmethod
    def obtener_proveedores(cls):
        return [prov for prov in cls.proveedores]

# Facturacion

    @classmethod
    def generar_factura(cls, producto: dtoProducto):
        datos_factura = {"valor producto": producto.valor_compra}
        factura: dtoFactura = dtoFactura(
            id=cls.ID_FACTURA, datos=datos_factura)

        valor_compra: float = producto.cantidad * producto.valor_venta

        descuento_nacimiento = cls.validar_descuento_nacimiento(
            producto.id)
        descuento_cantidad = cls.validar_descuento_cantidad(producto)

        if descuento_nacimiento:
            factura.datos["descuento cumpleaños"] = "20%"
            valor_compra = valor_compra*0.2

        if descuento_cantidad:
            factura.datos["descuento cantidad mismo producto"] = "25%"
            valor_compra = valor_compra*0.25

            factura.datos["valor total"] = valor_compra
        cls.ID_FACTURA += 1
        cls.facturas.append(factura)
        return factura

    @classmethod
    def obtener_facturas(cls):
        return [factura for factura in cls.facturas]
