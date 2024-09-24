x = int(input())

a = -1
lista = []

while len(lista) < 1000 and x >= 2 and x <= 50:
    while a < (x -1) and len(lista) < 1000:
        a = a + 1
        lista.append(a)
    a = -1
for i in range(len(lista)):
    print(f"N[{i}] = {lista[i]}")
