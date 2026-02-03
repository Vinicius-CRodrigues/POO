from Modelos.restaurante import Restaurante

# Tudo que EXECUTA lógica, cria objetos, imprime, muda estado 👉 deve ficar dentro do if __name__ == "__main__". Ela é usada para controlar quando o código deve ser rodado, protegendo assim os seus objetos e métodos.
# Ele garante que o código só execute quando o arquivo for rodado diretamente, e não quando for importado.
if __name__ == '__main__':
    
    # Aqui são criados e construídos os objetos.
    hut = Restaurante('pizza express', 'Italiana')
    nazo = Restaurante('sushi nazo', 'Japonesa')

    # Consigo mudar o nome somento com o _, pois nome está como protegido.
    hut._nome = 'Pizza Hut'
    hut.receber_avaliacao('Vinicius', 5)
    hut.receber_avaliacao('João', 5)

    # Quando uso a palavra vars, ela cria um dicionário e me demonstra as informações de cada atributo daquele objeto
    print(vars(hut))
    print(vars(nazo))

    print('-'*100)

    hut.alternar_status_por_hora()
    nazo.alternar_status_por_hora()

    # Listando as infromações da lista restaurantes_cadastrados.
    Restaurante.listar_restaurantes()