import requests
import re

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
json = response.json()
eur = json[0]
eurs = float(eur['sale'])
usd = json[1]
usds = float(usd['sale'])

a = (input("Выберите валюту которую ходите перевести:\n1 = Гривна\n2 = Доллар\n3 = Евро\n"))
while True:
    if re.match(r'^[123]{1}$', a):
        break
    a = input("Введите цифру от 1 до 3\n")
b = input("Выберите в какую валюты вы хотите перевести:\n1 = Гривна\n2 = Доллар\n3 = Евро\n")
    
while True:
    if a == b:
        b = input('Вы не можите выбрать одинаковые валюты!\n')
    elif re.match(r'^[123]{1}$', b):
        break
    else:
        b = input("Введите цифру от 1 до 3\n")
a = int(a)
b = int(b)
d = 'None'
while not d.isdigit():
    d = input("Ведите количество валюты которую хотите обменять:\n")
d = int(d)

if a == 1 and b == 2:
    print((d / usds), 'USD')
elif a == 1 and b == 3:
    print((d / eurs), 'EUR')
elif a == 2 and b == 1:
    print((usds * d), 'UAH')
elif a == 3 and b == 1:
    print((eurs * d), 'UAH')
elif a == 2 and b == 3:
    print((usds / eurs * d), 'EUR')
elif a == 3 and b == 2:
    print((eurs / usds * d), 'USD')