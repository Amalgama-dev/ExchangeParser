import requests

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
json = response.json()
eur = json[0]
eurs = float(eur['sale'])
usd = json[1]
usds = float(usd['sale'])


a = int(input("Выберите валюту которую ходите перевести:\n1 = Гривна\n2 = Доллар\n3 = Евро\n"))
print(a)
b = int(input("Выберите в какую валюты вы хотите перевести:\n1 = Гривна\n2 = Доллар\n3 = Евро\n"))
if a == b:
    b = int(input('Вы не можите выбрать одинаковые валюты!\nВыберите в какую валюты вы хотите перевести:\n1 = Гривна\n2 = Доллар\n3 = Евро\n'))
d = int(input("Ведите количество валюты которую хотите обменять:\n"))
if a == 1 and b == 2:
    print(d / usds)
elif a == 1 and b == 3:
    print(d / eurs)
elif a == 2 and b == 1:
    print(usds * d)
elif a == 3 and b == 1:
    print(eurs * d)
elif a == 2 and b == 3:
    print(usds / eurs * d)
elif a == 3 and b == 2:
    print(eurs / usds * d)