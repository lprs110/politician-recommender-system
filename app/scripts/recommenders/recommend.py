from app.scripts.recommenders.content_based_filtering import cb_recommend
from app.scripts.recommenders.collaborative_filtering import col_recommend
import sqlite3
from math import *

con = sqlite3.connect('storage.db', check_same_thread=False)
cur = con.cursor()


def Hybrid_Recommendation(id):
    user = cur.execute("select * from users where id=?", (id,)).fetchall()

    col_rec = col_recommend(user)

    rec = []

    max_rate = max(col_rec, key=lambda rate: rate[1])
    if ceil(max_rate[1]) >= 3.0:
        for i, t in enumerate(col_rec):
            if round(t[1]) >= 2.5:
                rec.append(t)
    else:
        for i, t in enumerate(col_rec):
            if round(t[1]) > 1.0:
                rec.append(t)

    hybrid_recommendation = cb_recommend(rec, user)

    return hybrid_recommendation
