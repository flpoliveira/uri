tipoOperacao = input()

matriz = []

for i in range (12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0.0
contador = 0
for i in range(12):
    for j in range(12):
        if (i + j >= 12 and j - i >= 1):
            soma += matriz[i][j]
            contador += 1
if(tipoOperacao == 'S'):
    print("%.1f" % soma)
else:
    print("%.1f" % (soma / contador))
