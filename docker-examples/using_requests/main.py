import requests
import time

url = 'https://www.wikipedia.org/'

print('START')

response = requests.get(url)
print(response.text)

print('END')

while True:
    print('SLEEPING')
    time.sleep(60)
