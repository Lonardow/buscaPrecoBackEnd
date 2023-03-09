

def fibonacci(quantidade):
    sequencia = []
    contador = 0
    val1 = 0
    val2 = 1
    while contador < quantidade:
        sequencia.append(val1)
        soma = val1+val2
        val1 = val2
        val2 = soma
        contador += 1
    print(sequencia)


fibonacci(10)
