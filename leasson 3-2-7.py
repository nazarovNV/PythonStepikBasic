dict={}
n=int(input())
for i in range(n):
    x=int(input())
    if x in dict:
        print(dict[x])
    else:
        dict[x]=f(x)
        print(dict[x])
