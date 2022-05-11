data_from_file = open ("text.txt", 'r')
data_string=data_from_file.read()
data_string=data_string.split()
print(data_string)

data_from_file.close()

data_string_decoded = []
i=0
dictionary_num_word={}

while i < len(data_string):
    data_string[i]=data_string[i].lower()
    i+=1
print(data_string)

for word in data_string:
    word=word.lower()
    if word not in dictionary_num_word:
        dictionary_num_word[word]=1
    else:
        dictionary_num_word[word] += 1
        #print(f"Слово '{word}' уже есть в словаре и его количество теперь равно {dictionary_num_word[word]}")
for k, v in dictionary_num_word.items():
    print (k, v)

print(max(dictionary_num_word))