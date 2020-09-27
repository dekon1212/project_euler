n = 2000000
summe, prim = 0, [True] * n
for p in range(2, n):
    if prim[p]:
        summe += p
        print(p)
        for i in range(p*p, n, p):
            prim[i] = False
print(summe)
