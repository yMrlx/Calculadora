print('projeto de calculadora.')

n1 = int(input('escolha um numero: '))
n2 = int(input('escolha o segundo numero: '))

soma = n1 + n2
subtração = n1 - n2
divisao = n1/n2
multiplicação = n1 * n2
potencia = n1**n2
resto = 5 % 2

print('1.soma.\n'
'2.subtração.\n'
'3.divisão.\n'
'4.multiplicação.\n'
'5.potenciação.\n'
'6.resto da divisão.')

resposta = int(input('oque voce quer saber? '))

if resposta == 1 or resposta == soma:
      print(f'a soma dos numeros {n1} e {n2} é igual a: {soma}.')
elif resposta == 2 or resposta == subtração:
      print(f'resultado da subtração entre {n1} e {n2} é: {subtração}.')
elif resposta == 3 or resposta == divisao:
      print(f'se dividirmos {n1} por {n2} o resultado final é: {divisao}.')
elif resposta == 4 or resposta == multiplicação:
      print(f'resultado da multiplicação entre {n1} e {n2} é: {multiplicação}.')
elif resposta == 5 or resposta == potencia:
      print(f'se elevarmos {n1} a {n2} obteremos o resultado de: {potencia}.')
else:
      print(f'se dividirmos {n1} por {n2} o resto será: {resto}.')