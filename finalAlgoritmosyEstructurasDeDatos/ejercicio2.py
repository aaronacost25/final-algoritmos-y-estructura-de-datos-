import random

def lanzar_moneda():
    """Lanza una moneda y devuelve Cara o Cruz al azar."""
    return random.choice(["Cara", "Cruz"])

def probar_suerte(resultado_moneda, lista_numeros):
    """Toma el resultado de la moneda y una lista de números.

    Si el resultado es "Cara", la lista se vacía y se informa al usuario.
    Si el resultado es "Cruz", la lista se conserva y se informa al usuario.
    """
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros


lista_numeros = [1, 2, 3, 4, 5]


resultado = lanzar_moneda()
print(f"Resultado del lanzamiento: {resultado}")

nueva_lista = probar_suerte(resultado, lista_numeros)
print(f"Estado final de la lista: {nueva_lista}")
