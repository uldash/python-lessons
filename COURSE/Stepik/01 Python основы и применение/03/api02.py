'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, 
выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа 
к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем
 все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к 

API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и 
получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно 
выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

import requests
import json

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
 
Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, как 
осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)


Примечание:
В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra

Примечание для пользователей Windows
При открытии файла для записи на Windows по умолчанию используется кодировка CP1251, в то время как для записи имен на 
сайте используется кодировка UTF-8, что может привести к ошибке при попытке записать в файл имя с необычными символами.
 Вы можете использовать print, или аргумент encoding функции open.

 Get a token
 curl -v -X POST "https://api.artsy.net/api/tokens/xapp_token?client_id=196fe04747dace4fb454&client_secret=2677d281bb97360d3f6410dce7a78f8f"
 '''
import requests

Client_id = "196fe04747dace4fb454"
Client_secret = "2677d281bb97360d3f6410dce7a78f8f"
Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTUzMjY5NDY4OSwiaWF0IjoxNTMyMDg5ODg5LCJhdWQiOiI1YjUxZDYyMGNmNDRjZTYyOWQzY2NhMDYiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWI1MWQ2MjFjYWUyZTQ0YTY4NzJmMzhiIn0.51pvZA2je_3Jc6c_-elGaZ9MWGHq35XhEvOeJfPntBE"

headers = {"X-Xapp-Token": Token}
Dataset_name = "dataset_24476_4.txt"
Api_url = "https://api.artsy.net/api/artists/"
param = {"client_id": Client_id, "client_secret": Client_secret}
artists = list()

with open("dataset_24476_4.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        # print(line.strip())
        res = requests.get(Api_url + line.strip(), headers=headers)
        data = res.json()
        #print(line.strip(), data["sortable_name"], data["birthday"])
        artists.append([data["sortable_name"], data["birthday"]])
artists.sort(key=lambda val: val[1] + val[0])
print('\n'.join(i[0] for i in artists))
