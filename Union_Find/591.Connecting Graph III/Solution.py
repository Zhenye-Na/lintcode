class ConnectingGraph3:
    
    def __init__(self, n):
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i
        self.size = n

    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a = self._find(a)
        root_b = self._find(b)
        if root_b != root_a:
            self.father[root_a] = root_b
            self.size -= 1

    def _find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.size
