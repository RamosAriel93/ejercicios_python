class Vehiculo:
    def __init__(self, marca, modelo, cilindrada, color):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.color = color

    def arranca(self):
        print('El vehiculo ', self.marca, self.modelo, self.cilindrada, self.color, 'se puso en marcha correctamente.')


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada, color):
        super().__init__(marca, modelo, cilindrada, color)

    def arranque_moto(self):
        print('la moto ', self.marca, self.modelo, self.cilindrada, self.color, 'se puso en marcha correctamente.')


mi_moto = Moto('suzuki', 'Gn', 150, 'negro')
mi_moto2 = Moto('zanella', 'due', 150, 'blanca')

mi_moto.arranque_moto()
mi_moto2.arranque_moto()

