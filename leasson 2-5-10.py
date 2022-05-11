i = 0
a = [int(i) for i in input().split()]
b = []
while i < len(a):
    if i == 0 and len(a) != 1:
        b.append(a[-1] + a[i+1])
    elif i == 0 and len(a) == 1:
        b.append(a[0])
        break
    elif i != 0 and i != len(a) - 1:
        b.append(a[i-1] + a[i + 1])
    elif i != 0 and i == len(a) - 1:
        b.append(a[i-1] + a[0])
    i += 1

[print(i, end=" ") for i in b]