import sqlite3
import pandas as pd

con = sqlite3.connect('../../../storage.db')
cur = con.cursor()

df = pd.read_csv('../datasets/avaliacao.csv')
df.drop(['Timestamp'], axis=1, inplace=True)

sql_insert = 'insert into users values (NULL, ?, ?, ?)'

inserts = []
for index in df.index:
    aux = ("user" + str(index + 1), "User" + str(index + 1), 123456)
    inserts.append(aux)

for insert in inserts:
    cur.execute(sql_insert, insert)

con.commit()

print("Committed sucessfully.")

con.close()
