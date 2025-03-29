# DESAFIO 001 – Manipulando Strings e Entrada de Dados

"""
Crie um programa em Python que imprima a frase 'Hello, World' de diferentes maneiras:
Diretamente com o comando print().
Armazenando a mensagem em variáveis separadas, concatenando-as e imprimindo o resultado.
Usando diferentes métodos de formatação de strings (.format() e f-string).
Em seguida, peça para o usuário informar o dia, mês e ano do seu nascimento através da função input(). Imprima na tela uma mensagem formatada mostrando a data completa de duas maneiras diferentes (concatenação direta e usando vírgulas).
"""

print('Hello, World')
msg = 'Hello, World'
msg1 = 'Hello,'
msg2 = ' World'
msgsoma = msg1 + msg2
print(msg)
print('{}'.format(msg))
print(f'{msg1}{msg2}')
print(msgsoma)

day = input('Dia = ')
month = input('Mes = ')
year = input('Ano = ')
print('Vocé nasceu no dia ' + day + '/' + month + '/' + year + '. Correto?')
print('Vocé nasceu no dia ',day,'/',month,'/',year,'. Correto?')



