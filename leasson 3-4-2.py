data_from_file = open ("text.txt", 'r')
data_string=data_from_file.readline()
print(data_string)

data_from_file.close()

data_string_decoded = []
i=0
print(len(data_string))



while i < len(data_string)-1:
    if i+1 !=len(data_string)-1:
        if not data_string[i].isnumeric() and data_string[i+1].isdigit() and not data_string[i+2].isdigit():
            print("1")
            print(f"Индекс i равен {i}")
            data_string_decoded.append(data_string[i] * int(data_string[i + 1]))
            print(data_string)
            print(data_string_decoded)

        elif not data_string[i].isnumeric() and data_string[i+1].isdigit() and data_string[i+2].isdigit():
            print("2")
            print(f"Индекс i равен {i}")
            data_string_decoded.append(data_string[i] * (int(data_string[i + 1] + data_string[i + 2])))
            print(data_string)
            print(data_string_decoded)
        else:
            pass
        print("цикл пройден")
        i += 1
    if i+1 ==len(data_string)-1:
        print("1")
        print(f"Индекс i равен {i}")
        data_string_decoded.append(data_string[i] * int(data_string[i + 1]))
        print(data_string)
        print(data_string_decoded)
        i += 1

print(data_string_decoded)
print ("".join(data_string_decoded))

    #data_string_decoded.append(data_string[i]*int(data_string[i+1]))
    #print(data_string_decoded)
    #i+=2

