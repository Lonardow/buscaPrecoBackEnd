obj = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros':  19849.53
}


def percentual():
    valor_total_mensal = 0
    for chave in obj:
        valor_total_mensal += obj[chave]

    for chave in obj:
        valor_percentual = (obj[chave]/valor_total_mensal) * 100

        print(
            f'O valor percentual do faturamento de {chave} foi {valor_percentual:.2f}% ')


percentual()
