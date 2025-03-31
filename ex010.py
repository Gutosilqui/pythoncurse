# DESAFIO 010

"""
Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólars ela pode comprar.

Considere US$1,00 = R$3,27
"""
cambio_dolar = 5.18
cambio_euro = 6.36
cambio_btc = 250000

reais = float(input('Digite o valor disponível na carteira (em R$): '))

dollar = reais / cambio_dolar
euro = reais / cambio_euro
btc = reais / cambio_btc

print(f'Seu valor em dolares é US${dollar:.2f}')
print(f'Seu valor em Euros é €{euro:.2f}')
print(f'Seu valor em Bitcoin é {btc:.6f} BTC')
