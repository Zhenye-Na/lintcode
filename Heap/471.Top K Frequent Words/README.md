# 471. Top K Frequent Words

**Description**

Given a list of words and an integer k, return the top k frequent words in the list.

You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.

**Example**

Example 1:

```
Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 3
Output: ["code", "lint", "baby"]
```


Example 2:

```
Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 4
Output: ["code", "lint", "baby", "yes"]
```

**Challenge**

Do it in `O(nlogk)` time and `O(n)` extra space.


**Max Heap**

```python
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
```

**Min Heap**

```python
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
```