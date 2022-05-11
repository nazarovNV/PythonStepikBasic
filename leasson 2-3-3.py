a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a-1,b+1):
    if i == a-1:
        for j in range(c,d+1):
            if j == c:
                print(f"\t{c}\t", end="")
            else:
                print(f"{j}\t", end="")

    else:
        for j in range(c-1,d+1):
            if j == c-1:
                print(f"{i}\t", end="")
            else:
                print(f"{i*j}\t", end="")
    print()