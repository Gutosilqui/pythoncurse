"""
nome = input('Qual é o seu nome?')
print(f'Nome:{nome*20}.')
print(f'Nome:{nome:<20}.')
print(f'Nome:{nome:>20}.')
print(f'Nome:{nome:^20}.')
"""

"""
n1 = int(input('Digite um número = '))
n2 = int(input('Digite outro número = '))
print(f'A soma é {n1+n2}.')
"""

n1 = int(input('Digite um número = '))
n2 = int(input('Digite outro número = '))
soma = n1+n2
subtraçao = n1-n2
divisao = n1/n2
inteiro = n1//n2
resto = n1%n2
potencia = n1**n2
print(f'A soma dos numeros é {soma}.', end=' >>> ')
print(f'A subtração é {subtraçao}')
print(f'A divisão é \n{divisao:.3f}')
print(f'A divisão inteira é {inteiro}')
print(f'O resto da divisão é {resto}')
print(f'A potência é {potencia}')