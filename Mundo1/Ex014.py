#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
print('------CALCULADORA DE CONVERSÃO DE °C PARA °F------')
c = float(input('Digite os graus(°C): '))

f = (c * (9 / 5) + 32)
print(f'A temperatura {c: .2f}°C equivale a {f: .2f}°F')