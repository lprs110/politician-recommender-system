import sqlite3

con = sqlite3.connect('../../../storage.db')
cur = con.cursor()

sql_insert = 'insert into areas values (NULL, ?, ?)'

areas = [
    ["cultura", "Cultura"],
    ["economia", "Economia"],
    ["educacao", "Educação"],
    ["meio_ambiente", "Meio Ambiente"],
    ["saude", "Saúde"],
    ["seguranca", "Segurança"],
    ["tecnologia", "Tecnologia"]
]

inserts = []
for area in areas:
    aux = (area[0], area[1])
    inserts.append(aux)

for insert in inserts:
    cur.execute(sql_insert, insert)

con.commit()

print("Committed sucessfully.")

con.close()
