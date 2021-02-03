'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''

import os


def is_py(lst):
    for file in lst:
        if file[-3:] == '.py':
            return True
    return False


s = set()
for files in os.walk('main'):
    if is_py(files[2]):
        s.add(files[0])
s = list(s)
s.sort()
# print('\n'.join(s))
with open('main.txt', 'w') as w:
    w.write('\n'.join(s))
'''
import os

for cur_dir, subdirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            print(cur_dir)
            break
'''
