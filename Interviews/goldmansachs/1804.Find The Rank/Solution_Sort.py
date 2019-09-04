class Solution:
    """
    @param scores: two dimensional array
    @param K: a integer
    @return: return a integer
    """

    def FindTheRank(self, scores, K):
        # write your code here
        tuple_scores = []
        for idx, score in enumerate(scores):
            tuple_scores.append([score, idx])

        sorted_scores = sorted(tuple_scores, key=lambda x: sum(x[0]))

        return sorted_scores[::-1][K - 1][1]
