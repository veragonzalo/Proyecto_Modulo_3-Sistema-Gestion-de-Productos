# Sistema de Gestion de Productos
# Descripción: Sistema modular para gestionar productos en consola

from modulos.menu import menu_principal
from modulos.funciones_utiles import login

# Función que ejecuta la bienvenida al sistema y llama a la funcion login ubicada en el archivo funciones_utlies.py
# Cada usuario esta asociado a un ROL distinto, existen 2: admin (clave:admin123) y usuario (clave: user123)
# Cada rol permite acceder a ciertas opciones del Menu Principal

def main():
    print("=" * 50)
    print("🔐 Bienvenido al sistema de Gestión de Productos")
    print("=" * 50, "\n")

    print("Por favor ingrese usuario y contraseña:")
    rol_usuario = login()

    if rol_usuario is None:
        return

    menu_principal(rol_usuario)

if __name__ == "__main__":
    main()
