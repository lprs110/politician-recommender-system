import sqlite3
import pandas as pd

con = sqlite3.connect('../../../storage.db')
cur = con.cursor()

df = pd.read_csv('../datasets/avaliacao.csv')

df.drop(['Timestamp'], axis=1, inplace=True)
df.index = range(1, len(df) + 1)
df.columns = ['alckmin', 'amoedo', 'bolsonaro', 'boulos', 'ciro', 'marina', 'haddad', 'daciolo']

sql_insert = 'insert into user_candidates values (?, ?, ?)'

inserts = []

for index, row in df.iterrows():

    user = "user" + str(index)

    for cand, rate in row.iteritems():

        user_id = cur.execute("select id from users where username=?", (user,)).fetchall()[0][0]
        cand_id = cur.execute("select id from candidates where candname=?", (cand,)).fetchall()[0][0]

        aux = (user_id, cand_id, rate)

        inserts.append(aux)

for insert in inserts:
    cur.execute(sql_insert, insert)

con.commit()

print("Committed sucessfully.")

con.close()
