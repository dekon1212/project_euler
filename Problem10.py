n = 2000000
    sum, prim = 0, [True] * n
    for p in range(2, n):
        if prim[p]:
            sum += p
            print(p)
            for i in range(p*p, n, p):
                prim[i] = False
    print(sum)
