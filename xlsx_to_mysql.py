import pandas as pd
from ezmysql import ConnectionSync

host = '124.223.224.49'
database = 'doubanTop250'
user = 'root'
password = '1486922887'
# create connection
db = ConnectionSync(
    host,
    database,
    user,
    password,
)

data=pd.read_excel('top250.xlsx')
data_dict = data.to_dict(orient='records')

for i in data_dict:
    db.table_insert('main',i)

db.close()
