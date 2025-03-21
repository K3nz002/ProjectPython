from datetime import datetime
import requests

def tabuada_7():
    for contador in range(0, 101):
        print (f'{contador} x 7 = {contador * 7}')

def contador_ate_100():
    for contador in range(0, 101, 4):
        print(f'{contador}', end='; ')
    
def horario_atual():
    # horas, minutos, dia, mes e ano atual
    hora_atual = datetime.now().hour
    minuto_atual = datetime.now().minute
    dia_atual = datetime.now().day
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # conversão do mês em extenso
    meses_extenso = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
     'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    mes_atual = meses_extenso[mes_atual - 1]

    print(f'São {hora_atual} : {minuto_atual} do dia {dia_atual} de {mes_atual} de {ano_atual}')
    
def cotacao_moedas():
    # API das cotações de moedas estrangeiras e bitcoin
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    lista_cotacoes = cotacoes.json()
    cotacao_dolar = float(lista_cotacoes['USDBRL']['bid'])
    cotacao_euro = float(lista_cotacoes['EURBRL']['bid'])
    cotacao_btc = float(lista_cotacoes['BTCBRL']['bid'])

    print('Escolha uma moeda:\n1. Dólar\n2. Euro\n3. Bitcoin')
    moeda = int(input())
    match moeda:

        case 1:
            print('Escolha a operação que gostaria de fazer\n1. USD -> Real\n2. Real -> USD')
            operacao = int(input())
            match operacao:

                case 1:
                    while True:
                        valor_dolar = float(input('Digite o valor em dólar: '))
                        print(f'O valor de dólar para real é R${valor_dolar * cotacao_dolar: .2f}')
                        if valor_dolar == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para dólar é ${valor_real / cotacao_dolar: .2f}')
                        if valor_real == 0:
                            break

        case 2:
            print('Escolha a operação que gostaria de fazer\n1. EUR -> Real\n2. Real -> EUR')
            operacao = int(input())
            match operacao:

                case 1:
                    while True:
                        valor_euro = float(input('Digite o valor em euro: '))
                        print(f'O valor de euro para real é R${valor_euro * cotacao_euro: .2f}')
                        if valor_euro == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para euro é €{valor_real / cotacao_euro:.2f}')
                        if valor_real == 0:
                            break

        case 3:
            print('Escolha a operação que gostaria de fazer\n1. BTC -> Real\n2. Real -> BTC')
            operacao = int(input())
            match operacao:

                case 1:
                    while True:
                        valor_btc = float(input('Digite o valor em bitcoin: '))
                        print(f'O valor de bitcoin para real é R${valor_btc * cotacao_btc}')
                        if valor_btc == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para bitcoin é ₿{valor_real / cotacao_btc}')
                        if valor_real == 0:
                            break

def calculadora_simples():
    print('Escolha uma operação:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potência')
    operacao = int(input())
    numero1 = float(input('Digite o primeiro valor:'))
    numero2 = float(input('Digite o segundo valor:'))

    match operacao:

        case 1:
            print(f'O resultado da soma é:\n{numero1} + {numero2} = {numero1 + numero2: .2f}')

        case 2:
            print(f'O resultado da subtração é:\n{numero1} - {numero2} = {numero1 - numero2: .2f}')

        case 3:
            print(f'O resultado da multiplicação é:\n{numero1} x {numero2} = {numero1 * numero2: .2f}')

        case 4:
            print(f'O resultado da divisão é:\n{numero1} : {numero2} = {numero1 / numero2: .2f}')

        case 5:
            print(f'O resultado da potência é:\n{numero1} ^ {numero2} = {numero1 ** numero2: .2f}')

def temperatura():
    print('Escolha a unidade de temperatura que deseja converter:\n1. Celsius\n2. Fahrenheit\n3. Kelvin')
    unidade = int(input())
    temperatura = float(input('Digite a temperatura: '))

    match unidade:
        case 1: # celsius
            print(f'A temperatura de {temperatura}°C em Fahrenheit é {(temperatura * 1.8) + 32: .2f}°F')
            print(f'A temperatura de {temperatura}°C em Kelvin é {temperatura + 273.15: .2f}K')

        case 2: # fahrenheit
            print(f'A temperatura de {temperatura}°F em Celsius é {(temperatura - 32) / 1.8: .2f}°C')
            print(f'A temperatura de {temperatura}°F em Kelvin é {(temperatura - 32) * 5 / 9 + 273.15: .2f}K')

        case 3: # kelvin
            print(f'A temperatura de {temperatura}K em Celsius é {temperatura - 273.15: .2f}°C')
            print(f'A temperatura de {temperatura}K em Fahrenheit é {(temperatura - 273.15) * 1.8 + 32: .2f}°F')

# Programa principal
print('1. Tabuada do 7\n2. Contador de 0 a 100 de 4 em 4\n3. Hora atual\n4. Cotação de moedas para real\n5. Calculadora simples\n6. Conversor de temperatura')
opcao = int(input('Escolha uma opção: '))

match opcao:

    case 1:
        tabuada_7()

    case 2:
        contador_ate_100()

    case 3:
        horario_atual()

    case 4:
        cotacao_moedas()

    case 5:
        calculadora_simples()

    case 6:
        temperatura()