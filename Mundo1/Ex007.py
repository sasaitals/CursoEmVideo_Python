#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
print('---------CALCULADORA DE MÉDIA---------')
nome = input('Digite o seu nome: ')
n1 = float(input('Digite a nota das atividades: '))
n2 = float(input('Digite a nota da prova regimental(A1): '))
n3 = float(input('Digite a nota da prova parcial(A2): '))

m = (n1 + n2 + n3) / 3
print(f'A média do aluno {nome} é {m: .2f}!')