import time
import sys
from modulos.gestion_datos import USUARIOS

# Funcion que valida el ingreso de usuarios registrados
def login():
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        if usuario in USUARIOS and USUARIOS[usuario]["password"] == password:
            print(f"✅ Bienvenido {usuario}")
            return USUARIOS[usuario]["rol"]

        else:
            intentos -= 1
            print(f"❌ Credenciales incorrectas. Intentos restantes: {intentos}")

    print("🚫 Acceso bloqueado")
    return None

# Funcion que sale del sistema
def salir_del_sistema():

    print("\n👋 ¡Gracias por usar nuestro sistema. Vuelva pronto!!")
    print("Saliendo...")
    time.sleep(1)
    sys.exit()


# def pausa():
 #   input("\nPresione ENTER para continuar...")
