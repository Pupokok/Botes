# Текст в кодировку UTF-8
import json

ar = []

with open('matt.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('matt.json', 'w', encoding='utf-8') as e:
    json.dump(ar,e)