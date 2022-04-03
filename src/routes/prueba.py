from datetime import date
import email
from mimetypes import init


class Tienda():
    def __init__(self, usiario, catalogo, factura, proveedores):
        self.usuario: list = usiario
        self.catalogo: list = catalogo
        self.facturas: list = factura
        self.proveedores: list = proveedores

class Usuario():
    def __init__(self, email, nombre, apellido, direccion, producto_interes, fecha_nacimiento, password):
        self.email: Email = email
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.direccion: str = direccion 
        self.producto_interes: TipoProducto() = producto_interes
        self.fecha_nacimiento: date = fecha_nacimiento
        self.password: str = password 
        
class Producto():
    def __init__(self, id, descripcion, valor_compra, valor_venta, cantidad, categoria, genero):
        self.id: int = id
        self.descipcion: str = descripcion 
        self.valor_compra: float = valor_compra 
        self.valor_venta: float = valor_venta
        self.cantidad: int = cantidad
        self.categiria: TipoProducto() = categoria
        self.genero: Genero() = genero

class Proveedor():
    def __init__(self, id, nombre, email, telefono, producto):
        self.id: int = id
        self.nombre: str = nombre
        self.email: Email = email
        self.telefono: str = telefono
        self.producto: TipoProducto() = producto


class Ubicacion():
    def __init__(self, pais, ciudad, direccion):
        self.pais: Pais() = pais
        self.ciudad: Ciudad() = ciudad
        self.direccion: str = direccion

class Pais():
    def __init__(self, moneda):
        self.moneda: Moneda() = moneda

class Moneda():
    def __init__(self, nombre, sigla):
        self.nombre: str = nombre
        self.sigla: str = sigla

class Ciudad():
    def __init__(self):
        pass

class BaseUbicacion():
    def __init__(self, nombre, codigo):
        self.nombre: str = nombre
        self.codigo: Ciudad() = codigo

class Genero():
    def __init__(self, Masculino, Femenino):
        pass

class TipoProducto():
    def __init__(self, Medias, Gafas, Relojes, Gorras, Bolsos, Camisas, Pantalones, Zapatos, RopaInterios):
        pass
