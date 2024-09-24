linhaDesejada = int(input())
operacao = input()
soma = 0
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

for s in matriz[linhaDesejada]:
    soma += s

if operacao == "S":
    print(f"{(soma):.1f}")
elif operacao == "M":print(f"{(soma/12):.1f}")
