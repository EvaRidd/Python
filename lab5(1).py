import requests

api_token = '40410a14ece78bcff546ab33aac664ab'
params = {'q': 'Санкт-Петербург', 'appid': api_token, 'units': 'metric'}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
x = response.json()
a = x['weather'][0]['main']
b = x['main']['temp']
c = x['main']['humidity']
e = x['main']['pressure']
print('Погода в СПБ:')
print('Weather:', a)
print('Temperature:', b)
print('Humidity:', c)
print('Pressure:', e)