from pandas import read_csv

df = read_csv('example - 1.csv')
key_list = list([d for d in df['key']])
tmp = {}
for r in [(0, 84, '일반 현황'), (84, 135, '교육 과정'), (135, 165, '학생'), (165, 188, '교수'), (188, 224, '시설'),
          (224, 231, '경영, 재정')]:
    for i in range(r[0], r[1]):
        tmp[key_list[i]] = r[2]
k, v = df.items()
tmp = {}
for key, value in zip(k[1], v[1]):
    tmp[key] = value

from pymongo import MongoClient

client = MongoClient('mongodb://kamc_root:kamc123456qwer!@43.201.146.205:19999/?authMechanism=DEFAULT')
col = client.kamc.school
col.insert_one(tmp)
