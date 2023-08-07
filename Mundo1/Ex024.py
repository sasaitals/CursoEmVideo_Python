#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
print('---------INICIA COM "SANTO"---------')
c = str(input('Insira o nome da sua cidade: ')).strip()
print(c[:5].upper() == 'SANTO')
