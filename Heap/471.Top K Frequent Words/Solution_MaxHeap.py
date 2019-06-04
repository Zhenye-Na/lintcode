from heapq import heappush, heappop, heappushpop
from collections import defaultdict

class Item:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count < other.count


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        if not words or len(words) < k:
            return None

        mapping = defaultdict(int)
        heap = []
        for word in words:
            mapping[word] -= 1

        for word in mapping:
            item = Item(mapping[word], word)
            heappush(heap, item)

        results = []
        for _ in range(k):
            results.append(heappop(heap).word)

        return results
