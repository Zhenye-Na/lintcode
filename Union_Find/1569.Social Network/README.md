# 1569. Social Network

Description

Everyone has their online friends. Now there are `n` people and `m` friend relationships . Ask if any person can directly or indirectly contact all online people. If ok, return `"yes"`, else return `"no"`.

The friend relationship is represented by a array `a` and a array `b`, which means that `a[i]` and `b[i]` are a pair of friends.

- $1 \leq n \leq 5000$
- $1 \leq m \leq 10000$
- A person may be friends with himself

**Example**

Example 1

```
Input: n=4, a=[1,1,1], b=[2,3,4]
Output: "yes"
Explanation:
1 and 2, 3, 4 can be directly contacted
2, 3, 4 and 1 can be directly contacted, these 3 people can be indirectly contacted by 1
```

Example 2

```
Input: n=5, a=[1,2,4], b=[2,3,5]
Output : "no"
Explanation:
1,2,3 can be connected to each other
4,5 can communicate with each other
However, the two groups cannot be contacted. For example, 1 cannot contact 4 or 5
```

```python
class Solution:
    """
    @param n: the person sum
    @param a: the array a
    @param b: the array b
    @return: yes or no
    """
    def __init__(self):
        self.common = {}
        self.size = None

    def find(self, p):
        path = []
        while p != self.common[p]:
            path.append(p)
            p = self.common[p]

        for people in path:
            self.common[people] = p

        return p

    def connect(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.common[min(pa, pb)] = max(pa, pb)
            self.size -= 1


    def socialNetwork(self, n, a, b):
        # Write your code here
        for i in range(1, n + 1):
            self.common[i] = i

        self.size = n
        for pa, pb in zip(a, b):
            self.connect(pa, pb)

        return "yes" if self.size == 1 else "no"
```
