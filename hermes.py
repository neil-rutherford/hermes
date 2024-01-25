import requests
import schedule
import time

def getsend():
    try:
        get = requests.get('https://api.binance.us/api/v3/ticker/price?symbol=BTCUSDT')
        price = float(get.json()['price'])
        send = requests.post('http://btcathena.pythonanywhere.com/c', data={'password': '', 'price': price})
    except:
        pass

schedule.every().minute.at(":00").do(getsend)
schedule.every().minute.at(":30").do(getsend)

while True:
    schedule.run_pending()
    time.sleep(1)
