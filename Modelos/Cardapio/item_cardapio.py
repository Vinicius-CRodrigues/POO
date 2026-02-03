from abc import ABC, abstractmethod

# Como estamos herdando a classe ABC da biblioteca, a nossa classe tem que ser herança de ABC.
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco
        
    def __str__(self):
        return f'{self._nome} | R${self._preco:.2f}'
    
    # Criamos uma classe abstrata para todas as classes filhas terem esse método.
    # O mesmo método irá se comportar em cada classe de forma diferente(polimorfismo)
    @abstractmethod
    def aplicar_desconto(self):
        pass