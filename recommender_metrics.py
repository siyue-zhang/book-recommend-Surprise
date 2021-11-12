from surprise import accuracy
from collections import defaultdict

class RecommenderMetrics:

    def MAE(predictions):
        return accuracy.mae(predictions, verbose=False)

    def RMSE(predictions):
        return accuracy.rmse(predictions, verbose=False)

    def GetTopN(predictions, n, min_rating):
        # every user get top N recommended books
        topN = defaultdict(list)

        for user_id, book_id, actual_rating, estimated_rating, _ in predictions:
            if (estimated_rating >= min_rating):
                topN[user_id].append((book_id, estimated_rating))

        for user_id, ratings in topN.items():
            ratings.sort(key=lambda x: x[1], reverse=True)
            topN[user_id] = ratings[:n]

        return topN
    
    def HitRate(topN_predicted, left_out_predictions):
             
        # remove one topN book from user training data, recommend topN books in testing phase
        hits = 0
        total = 0

        for left_out in left_out_predictions:
            user_id = left_out[0]
            left_out_book_id = left_out[1]
            # Is it in the predicted top 10 for this user?
            hit = False
            for book_id, predicted_rating in topN_predicted[user_id]:
                if (left_out_book_id == book_id):
                    hit = True
                    break
            if (hit):
                hits += 1

            total += 1

        # Compute overall precision
        return hits/total
    
    def RatingHitRate(topN_predicted, left_out_predictions):
        hits = defaultdict(float)
        total = defaultdict(float)

        # For each left-out rating
        for user_id, left_out_book_id, actual_rating, estimated_rating, _ in left_out_predictions:
            # Is it in the predicted top N for this user?
            hit = False
            for book_id, predicted_rating in topN_predicted[user_id]:
                if (left_out_book_id == book_id):
                    hit = True
                    break
            if (hit) :
                hits[actual_rating] += 1

            total[actual_rating] += 1

        # Compute overall precision
        for rating in sorted(hits.keys()):
            print (rating, hits[rating] / total[rating])
    
    def CumulativeHitRate(topN_predicted, left_out_predictions, rating_cutoff=0):
        hits = 0
        total = 0

        # For each left-out rating
        for user_id, left_out_book_id, actual_rating, estimated_rating, _ in left_out_predictions:
            # Only look at ability to recommend things the users actually liked...
            if (actual_rating >= rating_cutoff):
                # Is it in the predicted top 10 for this user?
                hit = False
                for book_id, predicted_rating in topN_predicted[user_id]:
                    if (left_out_book_id == book_id):
                        hit = True
                        break
                if (hit):
                    hits += 1
                total += 1

        return hits/total

    def AverageReciprocalHitRank(topN_predicted, left_out_predictions):
        summation = 0
        total = 0
        # For each left-out rating
        for user_id, left_out_book_id, actual_rating, estimated_rating, _ in left_out_predictions:
            # Is it in the predicted top N for this user?
            hitRank = 0
            rank = 0
            for book_id, predicted_rating in topN_predicted[user_id]:
                rank = rank + 1
                if (left_out_book_id == book_id):
                    hitRank = rank
                    break
            if (hitRank > 0) :
                summation += 1.0 / hitRank

            total += 1

        return summation / total
    
    # What percentage of users have at least one "good" recommendation
    def UserCoverage(topN_predicted, rating_threshold=0):
        hits = 0
        users = []
        for user_id in topN_predicted.keys():
            hit = False
            if user_id not in users:
                users.append(user_id)
            for book_id, predicted_rating in topN_predicted[user_id]:
                if (predicted_rating >= rating_threshold):
                    hit = True
                    break
            if (hit):
                hits += 1
        return hits / len(users)
