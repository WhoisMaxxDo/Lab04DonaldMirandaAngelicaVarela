import random as rd

lstProductos = []

class Productos:
    def __init__(self, pcodigo, pnombre, pmarca, pprecio, pexistencias, pproveedor):
        self.codigo = pcodigo
        self.nombre = pnombre
        self.marca = pmarca
        self.precio = pprecio
        self.existencias = pexistencias
        self.provedor = pproveedor

    def __str__(self):
        return f"codigo: {self.codigo}, nombre: {self.nombre}, marca: {self.marca}, precio: {self.precio}, existencias: {self.existencias}, provedor: {self.provedor[" nombre"]}"

def submenu():
    while True:
        try:
            entrada = False
            global provedor
            codigoProveedor = rd.randrange(100, 199)
            print(f"seleccione el provedor")
            print("1.Alimentos Don Mayorga")
            print("2.Productos Personales CCJ")
            print("3.Productos Varios PSA")
            opcion = int(input("selecione el provedor: "))
            if opcion == 1:
                nombreProveedor = "Alimentos Don Mayorga"
                paisProveedor = "Ecuador"
                entrada = True
            elif opcion == 2:
                nombreProveedor = "Productos Personales CCJ"
                paisProveedor = "United States"
                entrada = True
            elif opcion == 3:
                nombreProveedor = "Productos Varios PSA"
                paisProveedor = "Colombia"
                entrada = True
            else:
                print("las opciones son entre 1 y 3!")
            if entrada:
                provedor = {
                    "codigo": codigoProveedor,
                    "nombre": nombreProveedor,
                    "pais": paisProveedor
                }
                break
            elif not entrada:
                print("vuelva a intentar!")
        except ValueError:
            print("valor no valido")
def agregarProducto():
    while True:
        try:
            cantidad = int(input("cuantos productos desea agregar?: "))
            for _ in range(cantidad):
                codigo = rd.randrange(1, 99)
                nombre = input("ingrese el nombre del producto: ")
                marca = input("ingrese la marca del producto: ")
                precio = input("ingrese el precio del producto: ")
                existencias = input("ingrese la cantidad de existencias del producto: ")
                submenu()
                producto = Productos(codigo, nombre, marca, precio, existencias, provedor)
                lstProductos.append(producto)
                print("producto agregado exitosamente")
            break
        except ValueError:
            print("valor no valido")





def actualizarPrecio():
    while True:
        try:
            encontrado = False
            buscar = int(input("ingrese el codigo del producto al que desea editar su precio: "))
            for p in lstProductos:
                if p.codigo == buscar:
                    encontrado = True
                    print(f"producto encontrado en la lista de productos!, precio actual {p.precio}")
                    nuevoPrecio = int(input("ingrese el nuevo precio: "))
                    p.precio = nuevoPrecio
            if not encontrado:
                print(f"producto no encontrado con el codigo: {buscar}")
            elif encontrado:
                print(f"precio cambiado exitosamente!")
                break
        except ValueError:
            print("el codigo debe ser un valor numerico!")



def eliminarProducto():
    while True:
        try:
            encontrado = False
            buscar = int(input("ingrese el codigo del producto al que desea eliminar: "))
            for p in lstProductos:
                if p.codigo == buscar:
                    encontrado = True
                    lstProductos.remove(p)
            if not encontrado:
                f"producto no encontrado con el codigo: {buscar}"
            elif encontrado:
                print(f"producto eliminado exitosamente!")
                break
        except ValueError:
            print("el codigo debe ser un valor numerico!")


def verProductos():
    for x in lstProductos:
        print(x)

def buscarProducto():
    while True:
        try:
            encontrado = False
            buscar = int(input("ingrese el codigo del producto al que desea ver su informacion: "))
            for p in lstProductos:
                if p.codigo == buscar:
                    encontrado = True
                    print(f"nombre: {p.nombre}, marca: {p.marca}, precio: {p.precio}, existencias: {p.existencias}, provedor: {p.provedor["nombre"]}")
            if not encontrado:
                print(f"producto no encontrado con el codigo: {buscar}")
            elif encontrado:
                break
        except ValueError:
            print("el codigo debe ser un valor numerico!")


def cargarProveedor():
    global provedor
    provedor = {}
    leerTxt = open("proveedor.txt")
    linea_de_proveedor = leerTxt.readline()
    lista_de_proveedor = linea_de_proveedor.split(',')
    for parametroProveedor in lista_de_proveedor:
        proveedorInfo = parametroProveedor.split(":")
        provedor[proveedorInfo[0]]=str(proveedorInfo[1])


def guardarInventario():
        nombreArchivo = "inventario.txt"
        with open(nombreArchivo, "w") as archivo:
            for p in lstProductos:
                archivo.write(f"codigo: {p.codigo}, nombre: {p.nombre}, marca: {p.marca}, precio: {p.precio}, existencias: {p.existencias}, {''.join(map(str, p.provedor["nombre"]))}\n")
        print(f"Los datos de los productos se han guardado en {nombreArchivo}.")

def cargarInventario():
    print("a continuacion se te preguntara el provedor x veces dependentiendo de la cantidad de productos importados del archivo txt")
    with open("exportacionInventario.txt") as archivo:
        for linea in archivo:
            cargarProveedor()
            codigo = rd.randrange(1, 99)
            nombre, marca, precio, existencias = linea.strip().split(",")
            producto = Productos(codigo, nombre, marca, precio, existencias, provedor)
            lstProductos.append(producto)
        print("datos almacenados correctamente!")

def menu():
    while True:
        try:
            print("1.agregar producto")
            print("2.eliminar producto")
            print("3.actualizar pecio de producto")
            print("4.listar productos")
            print("5.buscar producto")
            print("6.guardar inventario en archivo")
            print("7.cargar inventario desde archivo")
            print("8.salir")
            opcion = int(input("seleccione una opcion: "))
            if opcion == 1:
                agregarProducto()
            elif opcion == 2:
                eliminarProducto()
            elif opcion == 3:
                actualizarPrecio()
            elif opcion == 4:
                verProductos()
            elif opcion == 5:
                buscarProducto()
            elif opcion == 6:
                guardarInventario()
            elif opcion == 7:
                cargarInventario()
            elif opcion == 8:
                break
            else:
                print("las opciones son entre 1 y 8!")
        except ValueError:
            print("digite un valor numerico o no lo deje vacio!")

menu()