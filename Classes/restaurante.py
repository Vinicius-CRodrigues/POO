from datetime import datetime
from zoneinfo import ZoneInfo as zoneInfo
from Classes.avaliacoes import Avaliacoes

'''
Programação Orientada a Objetos (POO) é um paradigma que organiza o código em torno de objetos, que agrupam dados (atributos) e comportamentos (métodos) para modelar entidades do mundo real, facilitando o desenvolvimento de sistemas complexos, modulares e fáceis de manter, usando princípios como Encapsulamento, Herança, Polimorfismo e Abstração.

'''
class Restaurante:
    restaurantes_cadastrados = []
    #Método especial construtor:
    def __init__(self, nome, categoria):
        # Como convensão, é interessante deixar os atributos sempre protegidos com o uderline antes.
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        # Criando um conjunto de avaliações com a lista.
        self._avaliacoes = []
        Restaurante.restaurantes_cadastrados.append(self)

    # Destacando as informações do objeto, onde está alicado na memória, em formato de texto com esse método especial.
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # Com o @property eu defino como o atributo será acessado e interpretado.
    @property
    def status_restaurante(self):
        return '❌' if self._ativo else '✅'

    # Você usa @classmethod quando quer um método que trabalha com a classe (cls) em vez de trabalhar com os atributos da instância (self) 
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante:":<20} | {"Média das avaliações:":<20} | {"Categoria:":<21} | Status:')
        for restaurante in cls.restaurantes_cadastrados:
            print(f'{restaurante._nome:<20} | {restaurante.media_avaliacao:<21} | {restaurante._categoria:<21} | {restaurante.status_restaurante}')
    
    def alternar_status_por_hora(self):
        agora = datetime.now(zoneInfo('America/Sao_Paulo'))

        if 11 <= agora.hour <= 18:
            self._ativo = False
        
        # Dentro de um método, eu estou recebendo uma classe que foi importada.
    def receber_avaliacao(self, cliente, nota):
        if nota < 0 or nota <= 5:
            avaliacao = Avaliacoes(cliente, nota)
            self._avaliacoes.append(avaliacao)
    
    # Agora sou capaz de entender como o atributo será acessado e interpretado.
    @property
    def media_avaliacao(self):
        if not self._avaliacoes:
            return 'Sem avaliações'
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            qde_notas = len(self._avaliacoes)
            media = soma_notas / qde_notas
            return f'{media:.1f}'
