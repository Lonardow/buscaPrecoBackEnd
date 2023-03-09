import json

with open('.\\testevaga\\dados.json') as json_dados:
    dados = json.load(json_dados)

valores = []
x = 0
for x in range(len(dados)):
    valores.append(dados[x]['valor'])


def maior_menor():
    maior_valor = menor_valor = valores[0]

    for valor in valores:
        if valor == 0:
            continue
        elif valor < menor_valor:
            menor_valor = valor
        elif valor > maior_valor:
            maior_valor = valor

    print(
        f'O maior valor de faturamento ocorrido em uma dia do mês foi: R${maior_valor:.2f}')
    print(
        f'O maior valor de faturamento ocorrido em uma dia do mês foi: R${menor_valor:.2f}')


maior_menor()


def media():

    soma = 0
    contador = 0
    for valor in valores:
        if valor > 0:
            contador += 1
        soma += valor
    media_faturamento_mensal = soma/contador
    # print(f'A média dos valores é: {media_faturamento_mensal:.2f}')

    contador_maiorQmedia = 0
    for valor in valores:
        if valor >= media_faturamento_mensal:
            contador_maiorQmedia += 1
    print(
        f'O Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é: {contador_maiorQmedia}')


media()
