#O mesmo professor do desafio anterior quer sortear a ordem de apresentação do trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteteada.
import random

print('---------SORTEIO DA APRESENTEÇÃO---------')
n1 = str(input('Insira o nome do primeiro aluno: '))
n2 = str(input('Insira o nome do segundo aluno: '))
n3 = str(input('Insira o nome do terceiro aluno: '))
n4 = str(input('Insira o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)