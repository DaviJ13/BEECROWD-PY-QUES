x = float(input())
y = x
a = []
a.append(x)
while len(a) < 100:
    y = y/2
    a.append(y)

for i in range(len(a)):
    print(f"N[{i}] = {a[i]:.4f}")
