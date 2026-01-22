# Funcion que valida el valor o tipo de numero ingresado en el parametro precioal crear un nuevo producto
def validar_precio(precio):
    if precio <= 0:
        return False
    return True

# Funcion que valida el valor o tipo de numero ingresado en el parametro stock al crear un nuevo producto
def validar_stock(stock):
    return stock >= 0
