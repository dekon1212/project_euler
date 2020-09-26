num = int(input())
res = [int(x) for x in str(num)]
liste = []
x2 = len(res)
summe = 0
for i in range(0,x2):
    summe = res[i]
    for j in range(i+1,x2):
        summe = summe * res[j]
        if j == i+12:
            liste.append(summe)
            break
print("Max: ", max(liste)) 
