import sqlite3

con = sqlite3.connect('../../../storage.db')
cur = con.cursor()

sql_insert = 'insert into candidates values (NULL, ?, ?)'

candidates = [
    ['alckmin', 'Geraldo Alckmin'],
    ['amoedo', 'João Amoêdo'],
    ['bolsonaro', 'Jair Bolsonaro'],
    ['ciro', 'Ciro Gomes'],
    ['daciolo', 'Cabo Daciolo'],
    ['boulos', 'Guilherme Boulos'],
    ['haddad', 'Fernando Haddad'],
    ['marina', 'Marina Silva']
]

inserts = []
for cand in candidates:
    aux = (cand[0], cand[1])
    inserts.append(aux)

for insert in inserts:
    cur.execute(sql_insert, insert)

con.commit()

print("Committed sucessfully.")

con.close()
