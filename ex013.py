# DESAFIO 013

"""
Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Qual é o seu salario atual: '))
aumento = salario * 15 / 100
valor = salario + aumento
print(f'Seu aumento vai ser de R${aumento:.2f}.')
print(f'Seu salario total agora será de R${valor:.2f}.')