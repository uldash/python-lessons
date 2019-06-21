'''
Пройтись по указанному каталогу и всем подкатологам,
посмотреть, если в имени файла есть число,
перенести его в начало имени, искать только первое число.
Пример:

$ python files_rename.py 'E:\VIDEO\MULT\Маша и медведь\'

main YY XX.py -> XX main YY.py
main XXX.py -> XXX main.py

'''
import os
import sys
import re


def main(path):
    names = os.listdir(path)
    for name in names:
        fullname = os.path.join(path, name)
        if os.path.isfile(fullname):
            print(fullname)
            match = re.search(r'\d+', name)
            if match:
                if len(match[0]) == 1:
                    zero_symbol = '0'
                else:
                    zero_symbol = ''
                new_name = os.path.join(
                    path, zero_symbol + match[0] + ' ' +
                    re.sub(r'..Серия.\d+.', r'', name))
                print(new_name + '\n')
                os.rename(fullname, new_name)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
