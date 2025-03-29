# DESAFIO 003 – Operações Aritméticas e Conversão de Dados

"""
Escreva um programa em Python que leia dois números inteiros informados pelo usuário e exiba a soma desses números na tela. Realize essa operação de duas formas diferentes:
Convertendo os valores diretamente durante a leitura (utilizando int(input())).
Recebendo os valores como strings e fazendo a conversão posteriormente antes da soma.
"""
number1 = int(input('Primeiro número '))
number2 = int(input('Segundo número '))
soma = number1 + number2
print('A soma é ', soma)

n1 = input('Primeiro número ')
n2 = input('Segundo número ')
soma = int(n1) + int(n2)
print ('A soma é', soma)

