# -*- coding: utf-8 -*-
"""Aula5_Class.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N5MlrlLdCzW4_wMJST2w93_TBYsziXXr

### **CLASS**

* Dado Serial: sequencia de dados
"""

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