# PYTHON
_**Códigos feito por mim na Linguagem Python, com auxilio do Professor Gilberto da Aula Programação de Computadores/Banco de Dados**_

## SOBRE OS PROJETOS
### 🐍 Conceitos Básicos da Linguagem Python - AULA 1
- Aqui aprendemos sobre Entrada/Saída de Dados
- Variáveis tambem foram explicadas
- Alem da função ``eval()`` que resolve uma expressão de uma variável
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

### 🐍 Laços de Repetição + Jogo de Adiviação
- Treinamos mais sore as ``listas``
- Aprendemos sobre o ``for``
- Aprendemos sobre o ``while``
- Usamos uma **biblioteca** chamada ``random``
1. Aqui a parte de treinamento da sintaxe:
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
2. Aqui o jogo de adiviação
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
