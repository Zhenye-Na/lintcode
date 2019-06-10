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
