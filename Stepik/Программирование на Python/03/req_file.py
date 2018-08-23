# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:03:50 2018

@author: user
"""

import requests

root='https://stepic.org/media/attachments/course67/3.6.3/'
file='dataset_3378_3.txt'
with open(file) as u:
    file=u.readline().strip()
print(file)

r=requests.get(file)
file=r.text.strip()
print(root+file)

while file[:3] != 'We ':
    r=requests.get(root+file)
    file=r.text.strip()
    print(root+file)
print(file)
