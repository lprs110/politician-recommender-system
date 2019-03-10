import sqlite3
import pandas as pd

a = 1
b = 5


def normalize(x, min_, max_):
    return ((b - a) * ((x - min_) / (max_ - min_))) + a


con = sqlite3.connect('../../../storage.db')
cur = con.cursor()

df = pd.read_csv('datasets/candidate.csv')

df.rename(columns={'meio ambiente': 'meio_ambiente'}, inplace=True)
candidates = ['alckmin', 'amoedo', 'bolsonaro', 'ciro', 'daciolo', 'boulos', 'haddad', 'marina']
df.index = candidates

min_value = min(df.min())
max_value = max(df.max())

df = normalize(df, min_value, max_value)
dict_cand = df.T.to_dict()

sql_insert = 'insert into candidate_areas values (?, ?, ?)'

inserts = []
for candidate in dict_cand.keys():
    for area, tfidf in dict_cand[candidate].items():

        cand_id = cur.execute("select id from candidates where candname=?", (candidate,)).fetchall()[0][0]
        area_id = cur.execute("select id from areas where area_name=?", (area,)).fetchall()[0][0]

        aux = (cand_id, area_id, tfidf)

        inserts.append(aux)

for insert in inserts:
    cur.execute(sql_insert, insert)

con.commit()

print("Committed sucessfully.")

con.close()
