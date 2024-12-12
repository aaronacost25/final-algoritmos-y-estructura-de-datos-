class Personaje:
    
    real = False


harry_potter = Personaje()


harry_potter.especie = "Humano"
harry_potter.magico = True
harry_potter.edad = 17


print(f"Especie: {harry_potter.especie}")
print(f"Es mágico: {harry_potter.magico}")
print(f"Edad: {harry_potter.edad}")
print(f"Es real: {harry_potter.real}")
