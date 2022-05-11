i = 0
final_list = []
list = [int(i) for i in input().split()]
original_list = set(list)

for i in original_list:
    if list.count(i) > 1:
        final_list.append(i)

[print(i, end=" ") for i in final_list]

