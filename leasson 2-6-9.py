lst = list(map(int, input().split()))
x = int(input())
ind = 0
indexes = []
for i in lst:
    if i == x:
        indexes.append(ind)
    ind += 1

if indexes == []:
    print("Отсутствует")
else:
    [print(i, end=" ") for i in indexes]
