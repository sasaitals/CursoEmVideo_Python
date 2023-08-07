#Escreva um program que pergunte o salário de um funcionario e calcule o valor de seu aumento. Para salarios superiores a R$1.250,00, calcule o aumento de 10%. Para os infefriores ou iguais o aumento é de 15%.
print('---------AUMENTO DE SALÁRIO---------')
s = float(input('Insira o salário do funcionario: '))
if s > 1250:
    ns = s + ((10 / 100) * s)
    print(f'O funcionário recebeu 10% de aumento. Seu novo salário é de R${ns}!')
else:
    ns1 = s + ((15 / 100) * s)
    print(f'O funcionário recebeu 15% de aumento. Seu novo salário é de R${ns1}!')