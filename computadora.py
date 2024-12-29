from monitor import Monitor
from raton import Raton
from tecado import Teclado


class Computadora:
    contador_computadora = 0
    def __init__(self, nombre,monitor, teclasdo, raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclasdo
        self.raton = raton



    def __str__(self):
        return (f'\t{self.nombre}\n'
                f'\tID: {self.id_computadora}\n,'
                f'\tMonitor: {self.monitor}\n'
                f'\tTeclado: {self.teclado}\n'
                f'\tRaton: {self.raton}\n'
                )

if __name__ == '__main__':
    teclado2 = Teclado('hp', 'bluetooth')
    raton2 = Raton('hp', 'usb')
    monitor2 = Monitor('hp', '27p')
    computadora2 = Computadora('HP',monitor2,raton2,teclado2)
    print(computadora2)