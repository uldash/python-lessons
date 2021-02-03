import requests

res = requests.get('https://docs.python.org/3.7/')
print(res.status_code)
print(res.headers['Content-Type'])
print(res.headers)
# print(res.content)
# print(res.text)
