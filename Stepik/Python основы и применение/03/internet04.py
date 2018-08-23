'''
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > 
и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. 
То есть, это последовательность символов, которая следует сразу после символов протокола, 
если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
'''
import requests
import re

#html = input().strip()
#html = "http://pastebin.com/raw/7543p0ns"#3 test
html = "http://pastebin.com/raw/hfMThaGb"  #2 test
saits = set()

first_page = requests.get(html)
if first_page.status_code == 200:
    #raise Exception(first_page.text)
    #urls = re.findall(r"(<a.+href[\s]?=[\s]?[\"\'][\w\-]+.*?[\"\'])", first_page.text)
    #urls = re.findall(r"(<a.+href=[\"\'][\w\-]+.*?[\"\'])", first_page.text)
    urls = re.findall(r"(<a.+href=[\"\'].*?[\"\'].*>)", first_page.text)
    for url in urls:
        #print(url)
        sait = re.search(r"([\w\-\._]+\.(?!open)[\w]+)", url)
        if sait:
            saits.add(sait.group())
saits = sorted(saits)
print('\n'.join(saits))