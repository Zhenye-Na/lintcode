805. Maximum Association Set

# Description

Amazon sells books, every book has books which are strongly associated with it. Given `ListA` and `ListB`, indicates that `ListA[i]` is associated with `ListB[i]` which represents the book and associated books. Output the largest set associated with each other (output in any sort). You can assume that there is only one of the largest set.

- The number of books does not exceed `5000`.

Example

```
Example 1:
	Input: ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"]
	Output: ["abc","acd","bcd","dfe"]
	Explanation:
	abc is associated with bcd, acd, dfe, so the largest set is the set of all books
	
Example 2:
	Input: ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"]
	Output: ["d","e","f","g"]
	Explanation:
	The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]
```

**Union Find**

采用了强化班 `Union Find` 的模板, 同时做了一些改进, 方便处理问题

1. 首先是 `union / connect` 操作的时候, 谁做谁的爸爸的问题: `self.father[min(rootA, rootB)] = max(rootA, rootB)` 谁大谁是爸爸!
2. 添加了一个 `self.children` 在每次 `union / connect` 操作时, 同时合并 "孩儿们", 方便之后的操作
3. 看谁的 孩儿们 数组, 哪个长


```python
from collections import defaultdict

class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        if not ListA or not ListB or len(ListA) != len(ListB):
            return []

        books = list(set(ListA + ListB))
        self.father = {i : i for i in books}
        self.children = defaultdict(list)
        for book in books:
            self.children[book].append(book)

        for a, b in zip(ListA, ListB):
            self.connect(a, b)

        result, max_length = None, -1
        for leader, follower in self.children.items():
            if len(follower) > max_length:
                result = follower
                max_length = len(follower)

        return result

    def find(self, book):
        path = []
        while book != self.father[book]:
            path.append(book)
            book = self.father[book]

        for b in path:
            self.father[b] = book

        return book

    def connect(self, bookA, bookB):
        rootA, rootB = self.find(bookA), self.find(bookB)
        if rootA != rootB:
            self.father[min(rootA, rootB)] = max(rootA, rootB)
            self.children[max(rootA, rootB)].extend(self.children[min(rootA, rootB)])
            self.children[min(rootA, rootB)].clear()
```