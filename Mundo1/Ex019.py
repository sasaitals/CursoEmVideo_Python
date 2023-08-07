#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome delas e escrevendo o nome escolhido.

from random import choice
print('---------SORTEIO DOS ALUNOS---------')
n1 = str('Primeiro aluno')
n2 = str('Segundo aluno')
n3 = str('Terceiro aluno')
n4 = str('Quarto aluno')

lista = [n1, n2, n3, n4]
escolha = choice(lista)

print(f'O aluno escolhido foi: {escolha}')