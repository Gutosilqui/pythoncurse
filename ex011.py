# DESAFIO 012

"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2.
"""

altura = float(input(f'Qual é a altura da parede: '))
largura = float(input(f'Qual é a largura da parede: '))
area = (altura * largura)
tinta = area / 2
print(f'A área da parede é {area:.2f}m.')
print(f'Para pintar a parede é necessario {tinta:.2f} litros de tinta.')