import sqlite3
from math import *

con = sqlite3.connect('storage.db', check_same_thread=False)
cur = con.cursor()


def searchArea(list_of_tuples, area_id):
    for index, tuples in enumerate(list_of_tuples):
        if tuples[0] == area_id:
            return index

    return -1


def minkowski(rating1, rating2, r=1):
    distance = 0
    commonRatings = False

    for area_id, rate in rating1:
        index = searchArea(rating2, area_id)

        if index != -1:
            distance += pow(abs(rate - rating2[index][1]), r)
            commonRatings = True

    return pow(distance, 1 / r) if commonRatings else float('Inf')


def cb_recommend(recommendations, user):

    distances = []

    user_areas = cur.execute("select area_id, rate from user_areas where user_id=?", (user[0][0],)).fetchall()

    for cand_id, rate in recommendations:
        candidate_areas = cur.execute("select area_id, tfidf from candidate_areas where candidate_id=?", (cand_id,)).fetchall()
        distance = minkowski(user_areas, candidate_areas)
        distances.append((cand_id, distance))

    return sorted(distances, key=lambda candTuple: candTuple[1])
