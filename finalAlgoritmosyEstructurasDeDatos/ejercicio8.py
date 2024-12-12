class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo(color="rojo")


print(f"Caras del cubo: {Cubo.caras}")
print(f"Color del cubo: {cubo_rojo.color}")
