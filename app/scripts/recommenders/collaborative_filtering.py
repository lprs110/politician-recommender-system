import sqlite3
from math import *
from collections import Counter

con = sqlite3.connect('storage.db', check_same_thread=False)
# con = sqlite3.connect('../../../storage.db')
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


def findMinNeighbors(neighborhood):

    min_neighbors = []

    for neighbor in neighborhood:
        if neighbor[0] == 0.0:
            min_neighbors.append(neighbor[1])
        else:
            break

    if not min_neighbors:
        return [neighborhood[0][1]]
    else:
        return min_neighbors


def col_recommend(user):
    user = cur.execute(base_query, (user[0][0],)).fetchall()

    nearest_neighbors = findMinNeighbors(neighbors(user))

    candidate_counter, score_counter = [], {}

    for neighbor_id in nearest_neighbors:

        user_neighbor = cur.execute(base_query, (neighbor_id,)).fetchall()

        for _, cand_id, rate in user_neighbor:

            index = searchCandidate(user, cand_id)

            if index == -1:

                candidate_counter.append(cand_id)

                if score_counter.get(cand_id) is None:
                    score_counter[cand_id] = rate
                else:
                    score_counter[cand_id] += rate

    candidate_counter = Counter(candidate_counter)
    recommendations = []

    for cand_id in candidate_counter:
        recommendations.append((cand_id, score_counter[cand_id] / candidate_counter[cand_id]))

    return sorted(recommendations, key=lambda candidateTuple: candidateTuple[1], reverse=True)
