from datetime import datetime
from Modelos.Cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, medida):
        super().__init__(nome, preco)
        self._medida = medida

    def __str__(self):
        return super().__str__() + f' | {self._medida}'
    
    def aplicar_desconto(self):
        agora = datetime.now()

        if agora.strftime('%A') == 'Friday':
            self._preco -= (self._preco * 0.08)
