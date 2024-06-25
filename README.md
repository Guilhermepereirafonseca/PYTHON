# PYTHON
_**Códigos feito por mim na Linguagem Python, com auxilio do Professor Gilberto da Aula Programação de Computadores/Banco de Dados**_

## SOBRE OS PROJETOS
### 🐍 Conceitos Básicos da Linguagem Python - AULA 1
- Aqui aprendemos sobre Entrada/Saída de Dados
- Variáveis tambem foram explicadas
- Alem da função ``eval()`` que resolve uma expressão de uma variável.
  - perdão se a estruta não está bom, foi o começo meu na linguagem
```python

expressao_matematica = input("Digite uma expressão matematica: ")

resultado = eval(expressao_matematica)

print("O resultado é", resultado)

print("ETEC Jales")
print("Ola Mundo!")
print("01/03/2024")

a = 2
print(a)
b = 2 + 2
print(b)
c = "Guilherme"
print(c)

"""Some a + b"""

a = 10
b = 3
c = a + b
print(c)

valor1 = 50
valor2 = 10
soma = valor1 + valor2
subtraia = valor1 - valor2
multiplica = valor1 * valor2
divisao = valor1 / valor2
print("soma", soma)
print("subtraia", subtraia)
print("multiplica", multiplica)
print("divisao", divisao)

a = "Guilherme"
b = "Pereira"
c = "Fonseca é foda nékkkkkk"
print(a,b,c)

lista = [10, "Banana", 3]
# matrizes começa com numero 0,1,2,3...
print(lista[0])

# defina o tipo do numero a ser inserido
# não precisa perguntar sobre o string (texto)
# SOMA
valor1_1 = int(input("Insira1 um numero: "))
valor1_2 = int(input("Insira um numero: "))
soma = valor1_1 + valor1_2
print(soma)

# SUBTRAÇÃO
valor2_1 = int(input("Insira1 um numero: "))
valor2_2 = int(input("Insira um numero: "))
subtração = valor2_1 - valor2_2
print(subtração)

# MULTIPLICAÇÃO
valor3_1 = int(input("Insira1 um numero: "))
valor3_2 = int(input("Insira um numero: "))
multiplicação = valor3_1 * valor3_2
print(multiplicação)

# DIVISÃO
valor4_1 = float(input("Insira1 um numero: "))
valor4_2 = float(input("Insira um numero: "))
divisão = valor4_1 / valor4_2
print(divisão)

# POTENCIAÇÃO
valor5_1 = int(input("Insira1 um numero: "))
valor5_2 = int(input("Insira um numero: "))
potenciação = valor5_1 ** valor5_2
print(potenciação)
```

### 🐍 Laços de Repetição + Jogo de Adiviação - AULA 2
- Treinamos mais sore as ``listas``
- Aprendemos sobre o ``for``
- Aprendemos sobre o ``while``
- Usamos uma **biblioteca** chamada ``random``
1. **Aqui a parte de treinamento da sintaxe:**
```python
lista = [1, 2, 3, 4, 5]

# Laço 'for' para percorrer a lista:
print("Usando laço 'for': ")
for elemento in lista:
    print(elemento)

lista = [1, 2, 3, "gui", 5]

print("Usando laço 'for': ")
for elemento in lista:
    print(lista[3])

# Laço 'while' para imprimir os números de 1 a 5
# faz em sequencia, adicionando +=
# não é uma matriz, mas sim uma sequencia normal.
# \n = pula a linha.

print("\nUsando o laço 'while':")
contador = 1
while contador <= 100:
    print(contador)
    contador += 1
```
2. **Aqui o jogo de adiviação:**
```python
import random

# Gerar um número aleatório entre 1 e 100.
numero_aleatorio = random.randint(1, 100)

# Iniciar o loop de adivinhação:
adivinhou = False  # Booleano para controlar se o número foi adivinhado
tentativas = 0  # Contador de tentativas

print("Bem-vindo ao jogo de Adivinhação!!")
print("Tente adivinhar o número entre 1 e 100.")

# Enquanto o número não for adivinhado, o loop continua
while not adivinhou:
    # Pedir ao usuário para adivinhar
    tentativa = int(input("Digite o seu palpite: "))

    # Verificar se o palpite está correto
    if tentativa == numero_aleatorio:
        tentativas += 1
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        adivinhou = True  # Número foi adivinhado, sair do loop
    elif tentativa < numero_aleatorio:
        print("O número é maior, tente novamente.")
        tentativas += 1
    else:
        print("O número é menor, tente novamente.")
        tentativas += 1
```

### 🐍 Função + Calculadora - AULA 3
- Aqui praticamos bastante o ``def`` com ele que você cria funções no python
- Cada função e uma equação da calculadora (**Adição, Subtração, Multiplicação, Divisão
- Tambem criamos uma função **MENU** com condições e possiveís erros que pode acontecer (*``try/except``*)
```python

# (a,b) = são as variaveis.
# break interrope o loop, sai do programa.
# ==: significa '=' (igual)

def adicao(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def multiplicacao(num1, num2):
    return num1*num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro! divisão por 0!!"
    else:
        return num1 / num2

def menu():
    print("\n \t Calculadora - ETEC")
    print("\n1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    menu()
    escolha = input("\nEscolha uma operação (1-5):")
    if escolha == '5':
        print("Saindo da Calculadora!!!")
        break

    try:
        num1 = float(input("Digite o número 1:"))
        num2 = float(input("Digite o número 2:"))
    except ValueError:
        print("Insira o valor correto!!!")
        continue

    if escolha == '1':
        print("\nResultado:", adicao(num1, num2))
    elif escolha == '2':
        print("\nResultado", subtracao(num1, num2))
    elif escolha == '3':
        print("\nResultado", multiplicacao(num1, num2))
    elif escolha == '4':
        print("\nResultado", divisao(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
```

### 🐍 Projeto Boletim - AULA 4
- Aqui fizemos uma tabela que mostra as notas e média dos alunos
  - Nesse exemplo **4 Alunos**, mas e possivel modificar o código para ter mais
```python 

# Função para calcular a média das notas
# len (lenght) = tamanho
# [] = matriz/array

def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas) # conta a quantidade de notas
    return soma / quantidade

# Lista de disciplinas

disciplinas = ["Fundamentos de Banco de Dados", "Programação de Computadores"]

# Dicionário para armazenar as notas de cada disciplina

notas_por_disciplina = {}

# Solicitar e armazenar as notas de cada disciplina

for disciplina in disciplinas:
    notas_disciplina = []

    for i in range(4):  # Limitado a quatro notas por disciplina.
        nota = float(input(f"Digite a nota {i+1} de {disciplina}: "))
        notas_disciplina.append(nota)
    notas_por_disciplina[disciplina] = notas_disciplina

# Calcular a média geral e médias por disciplina.

medias_por_disciplina = {disciplina: calcular_media(notas) for disciplina, notas in notas_por_disciplina.items()}
media_geral = calcular_media(list(medias_por_disciplina.values()))

# Imprimir o boletim escolar

print("\n BOLETIM ESCOLAR")
print("===============================================================================")
print("{:<30} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Disciplina", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Média"))
print("-------------------------------------------------------------------------------")
for disciplina, notas in notas_por_disciplina.items():
    print("{:<30} {:<10} {:<10} {:<10} {:<10} {:<10.2f}".format(disciplina, notas[0], notas[1], notas[2], notas[3], medias_por_disciplina[disciplina]))
print("----------------------------------------------------------------------------------")
print("{:<30} {:<10.2f}".format("Média Geral", media_geral))
print("====================================================================================")
```

### 🐍 Class - AULA 5
- Aqui apredemos o conceitos da **Lógica orientada a Objetos** do Python
  - Conceito muito utilizado para entender _**Banco de Dados**_
```python

# Criando uma class pessoa e suas caracteristicas
# Esse programa ira calcular o IMC de uma 'pessoa'
    # (peso / altura) ^2
# tabulate = exibe o código em forma de tabela
# append = adiciona algo a lista
# print() = uma linha em branco
# Indice = Primary key (chave primaria)

from tabulate import tabulate

class Pessoa:
    codigo_sequencial = 1

    def __init__(self, nome, idade, peso, altura):
        self.codigo = Pessoa.codigo_sequencial
        Pessoa.codigo_sequencial += 1
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}, IMC: {self.calcular_imc():.2f}"

def inserir_pessoa(pessoas):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa (em kg): "))
    altura = float(input("Digite a altura da pessoa (em metros): "))
    pessoa = Pessoa(nome, idade, peso, altura)
    pessoas[pessoa.codigo] = pessoa
    print("Pessoa cadastrada com sucesso!\n")

def alterar_pessoa(pessoas):
    codigo = int(input("Digite o código da pessoa que deseja alterar: "))
    if codigo in pessoas:
        pessoa = pessoas[codigo]
        print("Pessoa encontrada:")
        print(pessoa)
        nome = input("Digite o novo nome da pessoa (deixe em branco para não alterar): ")
        idade = input("Digite a nova idade da pessoa (deixe em branco para não alterar): ")
        peso = input("Digite o novo peso da pessoa (deixe em branco para não alterar): ")
        altura = input("Digite a nova altura da pessoa (deixe em branco para não alterar): ")
        if nome:
            pessoa.nome = nome
        if idade:
            pessoa.idade = int(idade)
        if peso:
            pessoa.peso = float(peso)
        if altura:
            pessoa.altura = float(altura)
        print("Pessoa alterada com sucesso!\n")
    else:
        print("Pessoa não encontrada.\n")

def excluir_pessoa(pessoas):
    codigo = int(input("Digite o código da pessoa que deseja excluir: "))
    if codigo in pessoas:
        del pessoas[codigo]
        print("Pessoa excluída com sucesso!\n")
    else:
        print("Pessoa não encontrada.\n")

def listar_pessoas(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
    else:
        table = [["Código", "Nome", "Idade", "Peso (kg)", "Altura (m)", "IMC"]]
        for pessoa in pessoas.values():
            table.append([pessoa.codigo, pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura, pessoa.calcular_imc()])
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
        print()

def menu():
    pessoas = {}
    while True:
        print("1. Inserir pessoa")
        print("2. Alterar pessoa")
        print("3. Excluir pessoa")
        print("4. Listar pessoas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_pessoa(pessoas)
        elif opcao == "2":
            alterar_pessoa(pessoas)
        elif opcao == "3":
            excluir_pessoa(pessoas)
        elif opcao == "4":
            listar_pessoas(pessoas)
        elif opcao == "5":
            print("Saindo do Programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
```

### 🐍 Cadastro de Clientes - AULA 6
- Aqui e um backend de Cadastro de Clientes no Python
```python

# Cadastar > Listar
# TipoCliente precisa do ID(1,2,3), que ira na lista tipos_clientes
# global = funciona em todo o código
# for = listar/para
#                   ¹Atributos, ²Metodos

class Cliente:
    def __init__(self, cliente_id, nome, tipo_id):
        self.cliente_id = cliente_id
        self.nome = nome
        self.tipo_id = tipo_id

class TipoCliente:
    def __init__(self, tipo_id, nome):
        self.tipo_id = tipo_id
        self.nome = nome

tipos_clientes = []
clientes = []
cliente_id_counter = 1
tipo_id_counter = 1

# Funções CRUD para tipos de cliente
def cadastrar_tipo_cliente():
    global tipo_id_counter
    nome = input("Digite o nome do tipo de cliente: ")
    tipo_cliente = TipoCliente(tipo_id_counter, nome)
    tipos_clientes.append(tipo_cliente)
    tipo_id_counter += 1
    print("Tipo de cliente cadastrado com sucesso!")

def listar_tipos_clientes():
    print("Tipos de clientes cadastrados:")
    for tipo_cliente in tipos_clientes:
        print("ID:", tipo_cliente.tipo_id, "- Nome:", tipo_cliente.nome)

# Funções CRUD para clientes
def cadastrar_cliente():
    global cliente_id_counter
    nome = input("Digite o nome do cliente: ")
    listar_tipos_clientes()
    tipo_id = int(input("Digite o ID do tipo de cliente: "))
    tipo_existente = False
    for tipo_cliente in tipos_clientes:
        if tipo_cliente.tipo_id == tipo_id:
            tipo_existente = True
            break
    if not tipo_existente:
        print("Tipo de cliente não encontrado.")
        return
    cliente = Cliente(cliente_id_counter, nome, tipo_id)
    clientes.append(cliente)
    cliente_id_counter += 1
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    print("Clientes cadastrados:")
    for cliente in clientes:
        tipo_cliente = next((tipo.nome for tipo in tipos_clientes if tipo.tipo_id == cliente.tipo_id), "Desconhecido")
        print("ID:", cliente.cliente_id, "- Nome:", cliente.nome, "- Tipo:", tipo_cliente)

# Menu principal
def exibir_menu_principal():
    print("1 - Tipos de cliente")
    print("2 - Clientes")
    print("3 - Sair")

# Menu para tipos de cliente
def exibir_menu_tipos_clientes():
    print("\n--- Menu Tipos de Cliente ---")
    print("1 - Cadastrar tipo de cliente")
    print("2 - Listar tipos de cliente")
    print("3 - Voltar")

# Menu para clientes
def exibir_menu_clientes():
    print("\n--- Menu Clientes ---")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Voltar")

while True:
    exibir_menu_principal()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        while True:
            exibir_menu_tipos_clientes()
            opcao_tipo = int(input("Escolha uma opção: "))

            if opcao_tipo == 1:
                cadastrar_tipo_cliente()
            elif opcao_tipo == 2:
                listar_tipos_clientes()
            elif opcao_tipo == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 2:
        while True:
            exibir_menu_clientes()
            opcao_cliente = int(input("Escolha uma opção: "))

            if opcao_cliente == 1:
                cadastrar_cliente()
            elif opcao_cliente == 2:
                listar_clientes()
            elif opcao_cliente == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 3:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
```
