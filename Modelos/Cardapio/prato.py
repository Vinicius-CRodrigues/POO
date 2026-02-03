from datetime import datetime
from Modelos.Cardapio.item_cardapio import ItemCardapio

'''
A herança permite criar novas classes (subclasses) a partir de existentes (superclasses), herdando atributos e métodos para reutilizar código. O polimorfismo permite que objetos de tipos diferentes respondam à mesma mensagem (método) de maneiras distintas, garantindo flexibilidade e extensibilidade ao sistema. 
'''

# Inicio a classe Prato dizendo que ela passa a ser uma classe que herda os atributos e métodos da classe mãe ItemCardapio.
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # O super é um objeto especial que permite que nós acessamos as informações(métodos + atributos) de outra classe.
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        # Ele herda o método especial da classe mae e adiciona o novo atributo 
        return super().__str__() + f' | {self._descricao}'
    
    def aplicar_desconto(self):
        agora = datetime.now()

        if agora.strftime('%A') == 'Friday':
            self._preco -= (self._preco * 0.08)