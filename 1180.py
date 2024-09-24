N = int(input())
numeros = list(map(int, input().split()))

menor = numeros[0]
posicao = 0

for i in range(1, N):
    if numeros[i] < menor:
        menor = numeros[i]
        posicao = i

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
