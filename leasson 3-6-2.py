import requests
r = requests.get("https://apteka.magnit.ru/api/sale/basket/")
print(r.text)