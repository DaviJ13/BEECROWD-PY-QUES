a = []
for _ in range(20):
    x = int(input())
    a.append(x)
a.reverse()

for i in range(len(a)):
    print(f"N[{i}] = {a[i]}")
