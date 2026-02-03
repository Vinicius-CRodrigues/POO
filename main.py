from Modelos.restaurante import Restaurante
from Modelos.Cardapio.prato import Prato
from Modelos.Cardapio.bebida import Bebida

def main():
    # Criação dos objetos
    hut = Restaurante('pizza express', 'Italiana')
    nazo = Restaurante('sushi nazo', 'Japonesa')
    bomba = Prato('hamburger', 17.50, 'Melhor bomba da cidade')
    suco_caju = Bebida('suco de caju', 12, '1L')

    # Aplicando o desconto utilizando o método abstrato
    suco_caju.aplicar_desconto(), bomba.aplicar_desconto()

    hut._nome = 'pizza hut'

    hut.adicionar_no_cardapio(bomba)
    hut.adicionar_no_cardapio(suco_caju)

    hut.receber_avaliacao('Vinicius', 5)
    hut.receber_avaliacao('João', 5)

    hut.alternar_status_por_hora()
    nazo.alternar_status_por_hora()
    Restaurante.listar_restaurantes()
    hut.exibir_cardapio

# Tudo que EXECUTA lógica, cria objetos, imprime, muda estado 👉 deve ficar dentro do if __name__ == "__main__". Ela é usada para controlar quando o código deve ser rodado, protegendo assim os seus objetos e métodos.
# Ele garante que o código só execute quando o arquivo for rodado diretamente, e não quando for importado.
if __name__ == '__main__':
    main()
    
    # Quando uso a palavra vars, ela cria um dicionário e me demonstra as informações de cada atributo daquele objeto
    #print(vars(hut))
    #print(vars(nazo))
    