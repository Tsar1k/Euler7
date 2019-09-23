primelist = [2, 3]
n = 5
k = 2
while k != 10001:
    index = 0
    while primelist[index] < (n / 2):
        if n % primelist[index] != 0:
            index += 1
        else:
            break
    else:
        primelist.append(n)
        k += 1
    n += 2
print(primelist[-1])
print(len(primelist))
