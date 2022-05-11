
massive = []
massive.append(int(input()))
while sum(massive) != 0:
    massive.append(int(input()))
num_kv = [i * i for i in massive]
print(sum(num_kv))

