# DESAFIO 004 – Tipos Primitivos e Métodos de Validação

"""
Desenvolva um programa que leia um valor digitado pelo usuário (pode ser numérico ou texto) e exiba na tela as seguintes informações sobre esse valor:
O tipo primitivo do valor digitado (type()).
Se o valor é numérico (isnumeric()).
Se o valor é decimal (isdecimal()).
Se o valor é formado apenas por dígitos (isdigit()).
Se o valor é alfabético (isalpha()).
Se o valor é alfanumérico (isalnum()).
Se o valor está totalmente em maiúsculas (isupper()).
Se o valor está totalmente em minúsculas (islower()).
Se o valor contém somente espaços (isspace()).
Se o valor inicia com letra maiúscula (istitle()).
"""
valor = input('Digite qualquer coisa seja números ou palavras = ')
print(f'O tipo primitivo desse valor é {type(valor)}')

print(f'É númerico? {valor.isnumeric()}')
print(f'É decimal? {valor.isdecimal()}')
print(f'É dígito? {valor.isdigit()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Contém apenas espaços? {valor.isspace()}')
print(f'Começa com letra maiúscula? {valor.istitle()}')