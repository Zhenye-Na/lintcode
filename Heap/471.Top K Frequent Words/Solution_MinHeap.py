import heapq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        if k == 0: return []
        counts = {}
        for w in words:
            if w not in counts:
                counts[w] = 0
            counts[w] += 1
        
        heap = []
        for word, count in counts.items():
            item = Item(count,word)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)
        
        heap.sort()
        ans = []
        for i in range(len(heap)-1,-1,-1):
            ans.append(heap[i].word)
        return ans

class Item:
    def __init__(self,count,word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __gt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count > other.count
    
    def __eq__(self,other):
        return self.count == other.count and self.word == other.word
