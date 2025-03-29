# DESAFIO 002 – Entrada de Dados e Formatação

"""
Crie um programa que leia o nome do usuário através da função input() e em seguida exiba uma mensagem de boas-vindas personalizada utilizando três métodos diferentes para formatar a mensagem (concatenação simples, método .format() e separação por vírgula).
"""

name = input('Qual é o seu nome? ')
print('Olá ' + name + '! Prazer em te conhecer!')
print('Olá {}! Prazer em te conhecer!'.format(name))
print('Olá', name,'! Prazer em te conhecer!')

