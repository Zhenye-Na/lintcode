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
