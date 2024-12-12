def suma_menores(lista_numeros):

    return sum(numero for numero in lista_numeros if 0 < numero < 1000)


lista_numeros = [150, -20, 300, 1200, 450, 1, 999]
resultado = suma_menores(lista_numeros)
print(f"La suma de los números válidos es: {resultado}")
