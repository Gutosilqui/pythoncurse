# DESAFIO 005

"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
number = int(input('Digite um número para saber seu antecessor e seu sucessor: '))
antecessor = number-1
sucessor = number+1
print(f'O número {number} tem como antecessor o {antecessor} e seu sucessor é {sucessor}.')
print(f'O número {number} tem como antecessor o {number-1} e seu sucessor é {number+1}.')