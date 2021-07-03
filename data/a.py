
import json

a = open('a.json')

x = json.load(a)
for d in x['data']['dataList']:
    print(d['dbName'], d['tableName'], d['tableComment'])
