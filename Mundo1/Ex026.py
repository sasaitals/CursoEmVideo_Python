#Faça um programa que leia uma frase pelo teclado e mostre:
#- Quantas vezes aparece a letra 'A'.
#- Em que posição ele aparece a primeira vez
#- Em que posição ele aparece a última vez
print('---------CONTAGEM DE LETRA "A"---------')
f = str(input('Insira uma frase qualquer: ')).upper().strip()
print(f'A letra aparece {f.count("A")} vezes.')
print(f'A primeira posição em que aparece é {f.find("A")+1}')
print(f'A últma posição em que aparece é {f.rfind("A")+1}')