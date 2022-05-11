a = []
n = int(input())
i = 1
while len(a) <= n:
    list_to_add = [i]*i
    a.extend(list_to_add)
    i+=1

[print(i, end=" ") for i in a[0:n]]