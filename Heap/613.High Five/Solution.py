import heapq
from collections import defaultdict

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        scores = defaultdict(list)
        for result in results:
            scores[result.id].append(result.score)

        avg = {}
        for student_id in scores:
            if len(scores[student_id]) >= 5:
                avg[student_id] = sum(heapq.nlargest(5, scores[student_id])) / 5
            else:
                avg[student_id] = sum(heapq.nlargest(len(scores[student_id]), scores[student_id])) / len(scores[student_id])

        return avg
