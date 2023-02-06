import requests 
import json

headers = {'s_token':'d840fdacbc97ad9dc7783858428d764e10e32e42807aefdb51a45a79873ee03d'}
response = requests.get('https://api.sympla.com.br/public/v3/events/1759428', headers=headers).text
print(response)

name = response[1]

print(name)
