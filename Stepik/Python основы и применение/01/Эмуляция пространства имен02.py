# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:59:32 2018

@author: user
"""

n = int(input())

parent = {"global": None}
vs = {"global": set()}

for _ in range(n):
    t, fst, snd = input().split()
    if t == "create":
        parent[fst] = snd
        vs[fst] = set()
    elif t == "add":
        vs[fst].add(snd)
    else:  # t == get
        while fst is not None:
            if snd in vs[fst]:
                break
            fst = parent[fst]
        print(fst)
