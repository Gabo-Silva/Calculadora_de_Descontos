# Importando minhas funções.
import desconto
# Loop infinito.
while True:
    res = ''
    # Menu
    print('-' * 50)
    print('CALCULADORA DE DESCONTOS'.center(50))
    print('-' * 50)
    # Chamando as funções, e recebendo os valores do produto e do desconto. E no final fazendo o cálculo para saber o novo valor do produto.
    valor = desconto.leiaFloat('Qual é o preço do produto? R$')
    print('-' * 50)
    desc = desconto.leiaInt('Valor do desconto: ')
    print('-' * 50)
    calc = desconto.descontoCalc(valor, desc)
    # Exibição das informações.
    print(f'O produto que custava R${valor:.2f}'.center(50))
    print(f'Com desconto de {desc}% vai custar R${calc:.2f}'.center(50))
    print('-' * 50)
    # Pergunta se usuário quer continuar, se sim, ele continua, se não, ele termina.
    while res not in ('S', 'N'):
        res = str(input('Quer continuar [S/N]? ').strip().upper())
        if res not in ('S', 'N'):
            print('ERRO! Opção inválida.')
            print('-' * 50)
    if res in 'N':
        break
# Fim
print('-' * 50)
print('OBRIGADO POR USAR A MINHA CALCULADORA DE DESCONTOS'.center(50))
print('-' * 50)
