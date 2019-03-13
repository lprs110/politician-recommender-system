import sqlite3
from math import *

con = sqlite3.connect('storage.db', check_same_thread=False)
cur = con.cursor()

base_query = "select * from user_candidates where user_id = (?)"


def searchCandidate(list_of_tuples, candidate):
    for index, tuples in enumerate(list_of_tuples):
        if tuples[1] == candidate:
            return index

    return -1


def minkowski(rating1, rating2, r=1):
    distance = 0
    commonRatings = False
    for _, cand_id, rate in rating1:
        index = searchCandidate(rating2, cand_id)

        if index != -1:
            distance += pow(abs(rate - rating2[index][2]), r)
            commonRatings = True

    return pow(distance, 1 / r) if commonRatings else float('Inf')


def neighbors(user):
    distances = []

    all_ids = cur.execute("select id from users where id != ?", (user[0][0],)).fetchall()

    for user_id in all_ids:

        user_rating = cur.execute(base_query, (user_id[0],)).fetchall()
        distance = minkowski(user, user_rating)
        distances.append((distance, user_id[0]))

    return sorted(distances, key=lambda userTuple: userTuple[0])


def col_recommend(user):

    user = cur.execute(base_query, (user[0][0],)).fetchall()

    list_of_recommendations = []

    nearest_neighbor = neighbors(user)[0][1]

    user_neighbor = cur.execute(base_query, (nearest_neighbor,)).fetchall()

    for _, cand_id, rate in user_neighbor:

        index = searchCandidate(user, cand_id)

        if index == -1:

            list_of_recommendations.append((cand_id, rate))

    return list_of_recommendations
