def leiaInt(msg):
    # Tentar ler um número inteiro, caso não seja, exibe uma mensagem de erro.
    while True:
        try:
            num = int(input(msg))
        except:
            print('ERRO! Valor digitado inválido.')
            print('-' * 50)
        else:
            # Caso o número seja menor que 0 ou maior que 100, exibe uma mensagem de erro.
            if num < 0 or num > 100:
                print('ERRO! Valor digitado inválido.')
                print('-' * 50)
            else:
                # Caso nenhum dos erros ocorra, o valor é retornado.
                return num


def leiaFloat(msg):
    while True:
        # Tentar ler um número flutuante, caso não seja, exibe uma mensagem de erro.
        try:
            num = float(input(msg))
        except:
            print('ERRO! Valor digitado inválido.')
            print('-' * 50)
        else:
            # Faz o cálculo das casas decimais, se tiver mais do que 2 casas decimais, exibe uma mensagem de erro.
            casas_decimais = str(num).split('.')
            if num < 0 or len(casas_decimais[1]) > 2:
                print('ERRO! Valor digitado inválido.')
                print('-' * 50)
            else:
                # Caso nenhum dos erros ocorra, o valor é retornado.
                return float(f'{num:.2f}')


def descontoCalc(v, d):
    # Faz o cálculo do desconto e do novo preço. E no fim o retorna.
    calc = v * (d / 100)
    return float(f'{v - calc:2f}')
