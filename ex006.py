# DESAFIO 006

"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
mult = int(input('Digite um número para saber o seu dobro, triplo é raiz quadrada: '))
dobro = mult*2
triplo = mult*3
raiz = mult**0.5
print(f'Seu número é {mult}, o dobro é {dobro}, o triplo é {triplo} e sua raiz quadrada é {raiz:.0f}.')
print(f'Seu número é {mult}, o dobro é {mult*2}, o triplo é {mult*3} e sua raiz quadrada é {mult**0.5:.0f}.')