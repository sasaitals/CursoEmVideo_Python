#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primero e último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza
print('---------VERIFICAÇÃO DE PRIMEIRO E ÚLTIMO NOME---------')
n = str(input('Insira o nome completo: '))
nome = n.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]}')
