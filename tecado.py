from dispositivos_entrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    cantodor_teclado = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.cantodor_teclado += 1
        self.id_teclado = Teclado.cantodor_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'\tID: {self.id_teclado},'
                f'\tMarca: {self.marca}'
                f'\tTipo Entrada: {self.tipo_entrada}')

if __name__ == '__main__':
    teclado1 = Teclado('hp', 'bluetooth')
    print(teclado1)