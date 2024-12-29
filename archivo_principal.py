from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from tecado import Teclado

if __name__ == '__main__':
    teclado2 = Teclado('hp', 'bluetooth')
    raton2 = Raton('hp', 'usb')
    monitor2 = Monitor('hp', '27p')
    computadora2 = Computadora('HP',monitor2,raton2,teclado2)
    computadoras1 =[computadora2]

    orden1 = Orden(computadoras1)

    print(orden1)