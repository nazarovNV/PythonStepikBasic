dictionary_num_word={}
some_text = [i for i in input().split()]


i=0
for word in some_text:
    word=word.lower()
    if word not in dictionary_num_word:
        dictionary_num_word[word]=1
    else:
        dictionary_num_word[word] += 1
        #print(f"Слово '{word}' уже есть в словаре и его количество теперь равно {dictionary_num_word[word]}")
for k, v in dictionary_num_word.items():
    print (k, v)