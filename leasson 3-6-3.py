import requests
data_from_file = open ("text.txt", 'r')
data_string=data_from_file.read()



while True:
    try:
        r = requests.get(data_string)
        text_from_file = r.text
        print(text_from_file)
    except:
        print(text_from_file)
        pass


