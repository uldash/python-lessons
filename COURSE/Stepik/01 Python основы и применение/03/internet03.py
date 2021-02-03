'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами 
внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти 
за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
'''
import requests
import re
htmlA = input().strip()
#htmlA = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
htmlB = input().strip()
#htmlB = "https://stepic.org/media/attachments/lesson/24472/sample2.html"

second_list = list()

first_page = requests.get(htmlA)
if first_page.status_code == 200:
    urls = re.findall(r".*(https:\/\/.*\.html).*?", first_page.text)
    for url in urls:
        second_page = requests.get(url)
        if second_page.status_code == 200:
            urls_2 = re.findall(r".*(https:\/\/.*\.html).*?", second_page.text)
            second_list.extend(urls_2)
else:
    print("No")

if htmlB in second_list:
    print("Yes")
else:
    print("No")
'''
import re
import requests

start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")
'''