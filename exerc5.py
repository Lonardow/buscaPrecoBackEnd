string = 'O rato roeu a roupa do rei de roma'
nova_str = ''
tam = len(string) - 1
for i in range(tam, -1, -1):
    nova_str += string[i]
print(nova_str)
