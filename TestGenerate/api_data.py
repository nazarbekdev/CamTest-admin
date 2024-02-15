import requests

url = 'http://54.89.91.243:8000/api/category'

data = requests.get(url)

print(data.json())
