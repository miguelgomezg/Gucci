import email

class Tienda():
    def __init__(self, usuario, catalogo, facturas, proveedores):
        self.usuario: list[usuario] = usuario
        self.catalogo: list[catalogo] = catalogo
        self.facturas: list = facturas
        self.proveedores: list = proveedores

class Usuario():
    def __init__(self, email, nombre, apellido, direccion, producto_interes, fecha_nacimiento, password):
        self.email: str = email
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.direccion: str = direccion
        self.producto_interes: TipoProducto() = producto_interes
        self.password: str = password

class Proveedor():
    def __init__(self, id, nombre, email, telefono, producto):
        self.id: int = id
        self.nombre: str = nombre
        self.email: Email = email
        self.telefono: str = telefono
        self.producto: TipoProducto() = producto

class Producto():
    def __init__(self, id, descripcion, valor_compra, valor_venta, cantidad, categoria, genero):
        self.id: int = id
        self.descripcion: str = descripcion
        self.valor_compra: float = valor_compra
        self.valor_venta: float = valor_venta
        self.cantidad: int = cantidad
        self.categoria: TipoProducto() = categoria
        self.genero: Genero() = genero

class Genero():
    def __init__(self, masculino, femenino):
        self.masculino: str = masculino
        self.femenino: str = femenino

class TipoProducto():
    def __init__(self, Medias, gafas, relojes, gorras, bolsos, camisas, pantalones, zapatos, ropainterior):
        pass

class Ubicacion():
    def __ini__(self, pais, ciudad, direccion):
        self.pais: Pais() = pais
        self.ciudad: ciudad() = ciudad
        self.direccion: str = direccion

class Pais():
    def __init__(self,moneda):
        self.moneda: moneda() = moneda

class Ciudad():
    def __init__(self) -> None:
        pass

class Moneda():
    def __init__(self, nombre, sigla):
        self.nombre: str = nombre
        self.sigla: str = sigla

class BaseUbicacion():
    def __init__(self, nombre, codigo):
        self.nombre: str = nombre
        self.codigo: Ciudad() = codigo