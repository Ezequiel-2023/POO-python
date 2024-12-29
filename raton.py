from dispositivos_entrada import DispositivosEntrada

class Raton(DispositivosEntrada):
    cantodor_ratones = 0
    def __init__(self, marca, tipo_entrada):
        Raton.cantodor_ratones += 1
        self.id_raton = Raton.cantodor_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'\tID: {self.id_raton},'
                f'\tMarca: {self.marca}'
                f'\tTipo Entrada: {self.tipo_entrada}')

if __name__ == '__main__':
    raton1 = Raton('hp', 'usb')
    print(raton1)