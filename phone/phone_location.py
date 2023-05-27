import requests
import sys


co = ''' 
 ____  _                        _                    _   _             
 |  _ \| |__   ___  _ __   ___  | |    ___   ___ __ _| |_(_) ___  _ __  
 | |_) | '_ \ / _ \| '_ \ / _ \ | |   / _ \ / __/ _` | __| |/ _ \| '_ \ 
 |  __/| | | | (_) | | | |  __/ | |__| (_) | (_| (_| | |_| | (_) | | | |
 |_|   |_| |_|\___/|_| |_|\___| |_____\___/ \___\__,_|\__|_|\___/|_| |_|
            use input with country code like this +1
 '''


print(co)

def check(num):
    url = f'http://apilayer.net/api/validate?access_key=e7602b0121bc8ba8e8ea2e0fc8dba556&number={num}&country_code=&format=1'
    data = requests.get(url).json()

    for i,u in data.items():
        if num == '':
            print('please write something')
            break
        elif num == 'exit':
            sys.exit()
        else:
            print(i.capitalize(),u)

while True:
    a = check(num=input('Add Num: '))

