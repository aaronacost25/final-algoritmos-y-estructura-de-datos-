class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos como un ave")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando como un pez")
    def poner_huevos(self):
        print("Poniendo huevos como un pez")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando como un mamífero")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    def poner_huevos(self):
        print("Poniendo huevos como un ornitorrinco")


ornitorrinco = Ornitorrinco()
print(f"Es vertebrado: {ornitorrinco.vertebrado}")
print(f"Tiene pico: {ornitorrinco.tiene_pico}")
print(f"Es venenoso: {ornitorrinco.venenoso}")
ornitorrinco.nadar()
ornitorrinco.caminar()
ornitorrinco.amamantar()
ornitorrinco.poner_huevos()
