import pymongo
from pymongo import MongoClient
from pandas import DataFrame
import plotly.express as px

client = MongoClient('mongodb://kamc_root:kamc123456qwer!@43.201.146.205:19999/?authMechanism=DEFAULT')
db = client['KAMC_EDU_학생']
years = range(2018, 2021)
data = []
for y in years:
    collection = db[f'{y}_입학학생수']
    for doc in collection.find():
        univ = doc['대학명']
        male = doc['의예_남']
        female = doc['의예_여']
        data.append({'univ': univ, 'year': y, 'male': male, 'female': female})

df = DataFrame(data)
fig = px.pie(df, values='male', names='year')
