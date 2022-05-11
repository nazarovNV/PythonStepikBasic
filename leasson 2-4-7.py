DNK = "a"
i = 0
count = 0
DNK_modded = ""
while i < len(DNK):
    if i == 0 and len(DNK) != 1:
        count += 1
    elif DNK[i] == DNK[i-1] and i != len(DNK)-1:
        count += 1
    elif DNK[i] != DNK[i - 1]:
        DNK_modded = DNK_modded + DNK[i-1] + str(count)
        count = 1
    i += 1
if i == len(DNK) and DNK[i-1] != DNK[i-2]:
    count = 1
    DNK_modded = DNK_modded + DNK[i-1] + str(count)
elif i == len(DNK):
    count += 1
    DNK_modded = DNK_modded + DNK[i-1] + str(count)
print(DNK_modded)

