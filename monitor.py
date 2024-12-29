
class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self.id_monitor= Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano


    def __str__(self):
        return (f'\tID: {self.id_monitor},'
                f'\tMarca: {self.marca}'
                f'\tTipo Entrada: {self.tamano}')

if __name__ == '__main__':
    monitor1 = Monitor('hp', '12pulgadas')
    print(monitor1)