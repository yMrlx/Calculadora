print('projeto de calculadora.')

while True:
    try:  
        n1 = int(input('escolha um numero: '))
        n2 = int(input('escolha o segundo numero: '))
    except ValueError:
        print('escolha um numero!')
        continue

    soma = n1 + n2
    subtração = n1 - n2
    divisao = n1/n2
    multiplicação = n1 * n2
    potencia = n1**n2
    resto = n1 % n2

    print('1.adição.\n'
    '2.subtração.\n'
    '3.divisão.\n'
    '4.multiplicação.\n'
    '5.potenciação.\n'
    '6.resto da divisão.')

    resposta = input('Qual operação deseja relizar? ')

    if resposta == "1" or resposta.lower() == "adição":
        print(f'A soma dos números {n1} e {n2} é igual a: {soma}.')
    elif resposta == "2" or resposta.lower() == "subtração":
        print(f'Resultado da subtração entre {n1} e {n2} é: {subtração}.')
    elif resposta == "3" or resposta.lower() == "divisao":
        print(f'Se dividirmos {n1} por {n2} o resultado final é: {divisao}.')
    elif resposta == "4" or resposta.lower() == "multiplicação":
        print(f'Resultado da multiplicação entre {n1} e {n2} é: {multiplicação}.')
    elif resposta == "5" or resposta.lower() == "potenciação":
        print(f'Se elevarmos {n1} a {n2} obteremos o resultado de: {potencia}.')
    elif resposta == "6" or resposta.lower() == "resto da divisão":
        print(f'Se dividirmos {n1} por {n2} o resto será: {resto}.')
    else:
        print('Operação invalida!')

    novamente = input('Deseja utilizar a calculadora novamente? (s/n).')
    if novamente.lower() != "s":
        print('Obrigado, Até logo!')
        break



