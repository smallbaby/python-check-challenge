import json

names = list()
with open('a.txt','r',encoding='utf8') as f:
    i = 0
    for x in f.readlines():
            xx = json.loads(x)
            for d in xx['data']['dataList']:
                names.append(d['name'])


for x in names:
    print(x)

print(len(names))