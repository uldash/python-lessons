# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 19:55:59 2018

@author: user
"""
# Таки работает
# Таки без рекурсии


def _create(namespace, parent, d):
    d.update({namespace: {'parent': parent, 'vars': set()}})


def _add(namespace, var, d):
    d[namespace]['vars'].add(var)


def _get(namespace, var, d):
    nm = namespace
    while nm is not None:
        if var in d[nm]['vars']:
            break
        nm = d[nm]['parent']
    return nm


'''    if var in d[namespace]['vars']:
        return namespace
    elif d[namespace]['parent']==None and var not in d[namespace]['vars']:
        return None
    else:
        return _get(d[namespace]['parent'],var,d)
'''
outputlst = []
d = {'global': {'parent': None, 'vars': set()}}
n = int(input())
for i in range(n):
    cmd, nmsp, var = input().split()
    if cmd == 'create':
        _create(nmsp, var, d)
    elif cmd == 'add':
        _add(nmsp, var, d)
    if cmd == 'get':
        outputlst.append(_get(nmsp, var, d))
# print('\n',d)
for i in outputlst:
    print(i)
