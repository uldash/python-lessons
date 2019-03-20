# -*- coding: utf-8 -*-
'''
    Вызов программы должен содержать парметр
    python useargument [Name]
'''
import sys
import stdio


def main():
    stdio.write('Hi, ')
    stdio.write(sys.argv[1])
    stdio.writeln('. How are you?')


if __name__ == "__main__":
    main()
