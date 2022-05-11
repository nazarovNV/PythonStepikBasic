i = 0
list_1 = []
list_mod = []
list_1.append([i for i in input().split()])
i+=1
while list_1[i - 1] != ['end']:
    list_1.append([i for i in input().split()])
    i += 1

list_1.pop(i - 1)
i=0
j=0
while i != len(list_1):
    while j != len(list_1[i]):
        list_1[i][j] = int(list_1[i][j])
        j+=1
    j=0
    i += 1
#print(*list, sep="\n")

i=0
j=0
while i != len(list_1):
    if list_1[i] != None:
        list_mod.append([])
        while j != len(list_1[i]):
            list_mod[i].append(list_1[i][j])
            j+=1
    j = 0
    i += 1


i=0
j=0

while i != len(list_1):
    if len(list_1[0]) == 1 and len(list_1) == 1:
        list_mod = [[4]]
        break

    if len(list_1[0]) != 1 and len(list_1) == 1:
        while j != len(list_1[i]):
            if j == 0 and i == 0:
                list_mod[i][j] = list_1[i][j + 1] + list_1[i][-1] + list_1[i][j] + list_1[i][j]
            if j != 0 and j != len(list_1[i])-1:
                list_mod[i][j] = list_1[i][j + 1] + list_1[i][j - 1] + list_1[i][j] + list_1[i][j]
            if j == len(list_1[i]) - 1:
                list_mod[i][j] = list_1[i][0] + list_1[i][j - 1] + list_1[i][j] + list_1[i][j]
            j += 1
        break

    if len(list_1[0]) == 1 and len(list_1) != 1:
        #print(len(list_1))
        while i != len(list_1):
            if i == 0:
                list_mod[i][j] = list_1[i][0] + list_1[i][0] + list_1[-1][j] + list_1[i+1][j]
                #print("кейс1")
                #print(f"i равно {i}")
                #print(f"Матрица равна {list_mod}")
            elif i != 0 and i != len(list_1) - 1:
                #print("кейс2")
                list_mod[i][j] = list_1[i][j] + list_1[i][j] + list_1[i-1][j] + list_1[i+1][j]
                #print(f"i равно {i}")
                #print(f"Матрица равна {list_mod}")
            elif i == len(list_1) - 1:
                list_mod[i][j] = list_1[i][j] + list_1[i][j] + list_1[0][j] + list_1[i-1][j]
                #print("кейс3")
                #print(f"i равно {i}")
                #print(f"Матрица равна {list_mod}")
            i += 1
        break

    while j != len(list_1[i]):
        if j == 0 and i == 0:
            list_mod[i][j] = list_1[i][j + 1] + list_1[i][-1] + list_1[len(list_1) - 1][j] + list_1[i + 1][j]
        if j != 0 and j != len(list_1[i])-1 and i == 0:
            list_mod[i][j] = list_1[i][j + 1] + list_1[i][j - 1] + list_1[i + 1][j] + list_1[len(list_1) - 1][j]
        if j == len(list_1[i])-1 and i == 0:
            list_mod[i][j] = list_1[i][0] + list_1[i][j - 1] + list_1[i + 1][j] + list_1[len(list_1) - 1][j]

        if j == 0 and i !=0 and i != len(list_1)-1:
            list_mod[i][j] = list_1[i][j + 1] + list_1[i][-1] + list_1[i + 1][j] + list_1[i - 1][j]
        if j != 0 and j != len(list_1[i])-1 and i !=0 and i != len(list_1)-1:
            list_mod[i][j] = list_1[i][j + 1] + list_1[i][j - 1] + list_1[i + 1][j] + list_1[i - 1][j]
        if j == len(list_1[i]) - 1 and i !=0 and i != len(list_1)-1:
            list_mod[i][j] = list_1[i][0] + list_1[i][j - 1] + list_1[i + 1][j] + list_1[i - 1][j]

        if j == 0 and i == len(list_1)-1 :
            list_mod[i][j] = list_1[i][j + 1] + list_1[i][-1] + list_1[0][j] + list_1[i - 1][j]
        if j != 0 and j != len(list_1[i])-1 and i == len(list_1)-1 :
            list_mod[i][j] = list_1[i][j + 1] + list_1[i][j - 1] + list_1[0][j] + list_1[i - 1][j]
        if j == len(list_1[i])-1 and i == len(list_1)-1 :
            list_mod[i][j] = list_1[i][0] + list_1[i][j - 1] + list_1[0][j] + list_1[i - 1][j]

        j+=1
    j=0
    i += 1
i=0
j=0

while i != len(list_1):
    while j != len(list_1[i]):
        print(list_mod[i][j], end=' ')
        j+=1
    print()
    j = 0
    i += 1
