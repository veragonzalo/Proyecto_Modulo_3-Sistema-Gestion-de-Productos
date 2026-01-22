
from modulos.funciones_utiles import salir_del_sistema
from modulos.gestion_datos import (
    agregar_producto,
    listar_productos,
    buscar_producto,
    eliminar_producto,
    modificar_producto
)


# Función Menu Principal segun rol del usuario logeado

def menu_principal(rol_usuario):
    while True:
        print("\n**********************")
        print("    MENÚ PRINCIPAL    ")
        print("**********************")
        print("1. Listar productos")
        print("2. Buscar producto")

        if rol_usuario == "Admin":
            print("3. Agregar producto")
            print("4. Modificar producto")
            print("5. Eliminar producto")
            print("6. Salir")
        else:
            print("3. Salir")

        opcion = input("👉 Seleccione una opción: ")

        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3" and rol_usuario == "Admin":
            agregar_producto()
        elif opcion == "4" and rol_usuario == "Admin":
            modificar_producto()
        elif opcion == "5" and rol_usuario == "Admin":
            eliminar_producto()
        elif opcion == "6" and rol_usuario == "Admin":
            salir_del_sistema()
            break
        elif opcion == "3" and rol_usuario != "Admin":
            salir_del_sistema()
            break
        else:
            print("❌ Opción no válida o sin permisos")
