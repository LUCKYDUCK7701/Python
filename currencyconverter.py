import requests

API_KEY = 'fca_live_Pt067sVlsJqwlfRwBkn1QzuB7IqiHF7T6QY2R9Ma'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Pt067sVlsJqwlfRwBkn1QzuB7IqiHF7T6QY2R9Ma&currencies=EUR%2CUSD%2CCAD{API_KEY}"

CURRENCIES = ["USD","CAD","EUR","AUD","CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invaild Currency")
        return None
    
while True:
    base = input("Enter the base currency (q for quit): ").upper()
    
    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")