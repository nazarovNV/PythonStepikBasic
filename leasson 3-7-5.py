setClasses = tuple(str(i) for i in range(1, 12))
dictHeight = dict.fromkeys(setClasses, 0)
dictCount = dict.fromkeys(setClasses, 0)

with open('text.txt', encoding='UTF-8') as inf:
    for line in inf:
        lst = line.strip().split('\t')
        dictHeight[lst[0]] += float(lst[2])
        dictCount[lst[0]] += 1

for i in setClasses:
    if dictHeight[i] == 0:
        d = '-'
    else:
        d = str(dictHeight[i] / dictCount[i])
    print(i + ' ' + d)
