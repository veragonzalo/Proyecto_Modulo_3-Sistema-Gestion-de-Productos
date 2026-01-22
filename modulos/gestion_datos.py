from modulos.validaciones import validar_precio, validar_stock

productos = []  # Lista para almacenar cada producto nuevo incorporado
codigos = set() # Set para evitar códigos de productos duplicados

roles = ("Admin", "Usuario", "Invitado")  # Tupla para administrar roles de usuarios

USUARIOS = {
    "admin": {
        "password": "admin123",
        "rol": "Admin"
    },
    "usuario": {
        "password": "user123",
        "rol": "Usuario"
    }
}

# Funcion para agregar nuevos productos
def agregar_producto():
    codigo = input("Código del producto: ")

    if codigo in codigos:
        print("⚠️ El código ya existe")
        return

    nombre = input("Nombre del producto: ")

    try:
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("❌ Error: datos numéricos inválidos")
        return

    if not validar_precio(precio) or not validar_stock(stock):
        print("❌ Precio o stock inválido")
        return

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)
    codigos.add(codigo)

    print("✅ Producto agregado correctamente")

# Funcion para listar productos
def listar_productos():
    if not productos:
        print("📭 No hay productos registrados")
        return

    for p in productos:
        print(f"{p['codigo']} - {p['nombre']} | ${p['precio']} | Stock: {p['stock']}")

# Funcion para buscar productos dentro de los que existen en la lista
def buscar_producto():
    codigo = input("Ingrese código a buscar: ")

    for p in productos:
        if p["codigo"] == codigo:
            print(p)
            return

    print("❌ Producto no encontrado")

# Funcion para eliminar productos
def eliminar_producto():
    codigo = input("Código del producto a eliminar: ")

    for p in productos:
        if p["codigo"] == codigo:
            productos.remove(p)
            codigos.remove(codigo)
            print("🗑️ Producto eliminado")
            return

    print("❌ Producto no encontrado")

# Funcion para modificar productos
def modificar_producto():
    codigo = input("Ingrese el código del producto a modificar: ")

    for producto in productos:
        if producto["codigo"] == codigo:

            print("\nProducto encontrado:")
            print(producto)

            print("\n¿Qué desea modificar?")
            print("1. Nombre")
            print("2. Precio")
            print("3. Stock")
            print("4. Cancelar")

            opcion = input("Opción: ")

            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ")
                producto["nombre"] = nuevo_nombre

            elif opcion == "2":
                try:
                    nuevo_precio = float(input("Nuevo precio: "))
                    if validar_precio(nuevo_precio):
                        producto["precio"] = nuevo_precio
                    else:
                        print("❌ Precio inválido")
                        return
                except ValueError:
                    print("❌ Entrada inválida")
                    return

            elif opcion == "3":
                try:
                    nuevo_stock = int(input("Nuevo stock: "))
                    if validar_stock(nuevo_stock):
                        producto["stock"] = nuevo_stock
                    else:
                        print("❌ Stock inválido")
                        return
                except ValueError:
                    print("❌ Entrada inválida")
                    return

            elif opcion == "4":
                print("Operación cancelada")
                return

            else:
                print("❌ Opción inválida")
                return

            print("✅ Producto modificado correctamente")
            return

    print("❌ Producto no encontrado")

