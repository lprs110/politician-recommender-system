from app.scripts.recommenders.content_based_filtering import cb_recommend
from app.scripts.recommenders.collaborative_filtering import col_recommend
import sqlite3

con = sqlite3.connect('storage.db', check_same_thread=False)
cur = con.cursor()


def Hybrid_Recommendation(id):
    user = cur.execute("select * from users where id=?", (id,)).fetchall()

    col_recommendations = col_recommend(user)

    hybrid_recommendation = cb_recommend(col_recommendations, user)

    return hybrid_recommendation
