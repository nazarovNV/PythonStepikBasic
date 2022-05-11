import requests
data_from_file = open ("text.txt", 'r')
data_string=data_from_file.read()
print(data_string)
r = requests.get(data_string.strip())
text_from_file=r.text
text_from_file=text_from_file.splitlines()
print(len(text_from_file))