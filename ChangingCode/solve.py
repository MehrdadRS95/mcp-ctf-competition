import requests
from threading import Thread

HOST = 'https://localhost:27758'

array = ['' for i in range(1, 11)]

def get(num: int):
    r = requests.get(HOST + f"/{str(num)}", verify=False).text
    array[num - 1] = r
    
for i in range(1, 11):
    Thread(target=get, args=[i,]).run()
    
access_code = ''.join(array)

flag = requests.post(HOST + '/flag', params={'flag': access_code}, verify=False).text
print(flag)