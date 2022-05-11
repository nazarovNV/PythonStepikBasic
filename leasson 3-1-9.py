def modify_list(l):
	i = 0

	while i < len(l):
		if l[i]%2 !=0:
			l.pop(i)
			i-=1
		i+=1
	i=0
	while i < len(l):
		if l[i]%2 ==0:
			l[i] = l[i]//2
		i+=1
	return




lst = [1, 1, 4, 4]
modify_list(lst)
print(lst)
