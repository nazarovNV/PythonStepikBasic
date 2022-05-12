import requests
data_from_file = open ("text.txt", 'r')
data_string=data_from_file.read()
r = requests.get(data_string)
data_string = r.text


while True:
    try:
        r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+data_string)
        data_string = r.text
        print(data_string)
    except:
        print(data_string)
        pass


