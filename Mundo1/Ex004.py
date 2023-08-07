#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.

text = input('Digite qualquer tipo de texto: ')
print('O tipo primitivo desse valor é: ', type(text))
print('Só tem espaço? ', text.isspace())
print('É um número? ', text.isnumeric())
print('É alfabético? ', text.isalpha())
print('É alfanumerico? ', text.isalnum())
print('Está em maiúsculas? ', text.isupper())
print('Está em minúsculas? ', text.islower())
print('Está capitalizada? ', text.istitle())

