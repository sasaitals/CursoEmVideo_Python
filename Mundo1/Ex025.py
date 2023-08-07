#Crie um programa que leia o nome e diga se ela tem 'SILVA' no nome.
print('---------TEM "SILVA" NO NOME---------')
n = str(input('Insira seu nome completo: ')).strip()
print(f'Seu nome tem Silva? {"silva" in n.lower()}')