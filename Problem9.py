x = int(input())
count = False
for a in range(1,x):
    for b in range(1,x):
        c = x-a-b
        if not count:
            if (a**2+b**2) == c**2:
                print(a*b*c)
                count = True
