# DESAFIO 012

"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

produto = float(input('Valor do produto: '))
desconto = produto * 5 / 100
valor = produto - desconto
print(f'Ganhou 5% de desconto, valor final = {valor:.2f} ')
