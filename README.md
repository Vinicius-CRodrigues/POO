# 🍽️ Projeto: Catálogo de restaurantes.

Este repositório contém um projeto desenvolvido em Python focado na aplicação prática dos pilares da **Programação Orientada a Objetos (POO)**. O sistema simula o catálogo de restaurantes, permitindo cadastro, controle de status e processamento de avaliações.

---

## 🧠 Conceitos de POO Implementados

A Programação Orientada a Objetos organiza o código em torno de **objetos**, que agrupam dados (atributos) e comportamentos (métodos). Neste projeto, exploramos:

* **Encapsulamento:** Uso da convenção de atributos protegidos (`_nome`, `_categoria`) para controlar o acesso aos dados.
* **Abstração:** Modelagem da entidade "Restaurante" focando apenas nas propriedades essenciais para o negócio.
* **Composição:** A classe `Restaurante` interage com a classe `Avaliacoes`, demonstrando como objetos podem colaborar entre si.

---

## 🛠️ Tecnologias e Recursos Utilizados

### 1. Métodos Especiais (Dunder Methods)
* `__init__`: Método construtor que inicializa os atributos e registra a instância automaticamente na lista da classe.
* `__str__`: Fornece uma representação textual amigável do objeto.

### 2. Decoradores do Python
* `@property`: Utilizado para criar "atributos calculados", como o `status_restaurante` (exibe ícones dinâmicos) e a `media_avaliacao` (calcula a média das notas em tempo real).
* `@classmethod`: Permite que o método `listar_restaurantes` acesse dados da classe (`cls`) sem precisar de uma instância específica.

### 3. Manipulação de Tempo e Fuso Horário
* Utilização das bibliotecas `datetime` e `zoneinfo` para implementar regras de negócio baseadas no horário real (Fuso: America/Sao_Paulo).

---

## 📋 Funcionalidades Principais

* **Listagem Formatada:** Exibição organizada de todos os restaurantes, categorias e médias de avaliação.
* **Sistema de Avaliação:** Recebimento de notas de clientes com validação.
* **Controle de Funcionamento:** Alteração automática do status do restaurante com base na hora do dia.
