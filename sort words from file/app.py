#!/usr/bin/env python3

"""Программа сортировки слов длиной более 3х символов
"""

set_0 = set()

with open("text.txt", mode='r', encoding='utf-8') as f:
    I = iter(f.read().split(' '))
    for i in I:
        if len(i) > 3:
            for j in i:
                if not j.isalpha():
                    i = i.replace(j, ' ')

            i = i.strip()

            [set_0.add(f'{x.lower()} {x}') for x in i.split(' ') if len(x) > 3]


list_0 = sorted(list(set_0))

for k, v in enumerate(list_0):
    list_0[k] = list_0[k].split(' ')[1]

for i in list_0:
    print(i)
