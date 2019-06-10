class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def __init__(self):
        self.d = {}

    def connectedSet(self, nodes):
        # write your code here
        for n in nodes:
            self.d[n.label] = None

        for node in nodes:
            for n in node.neighbors:
                a = self.find_parent(node.label)
                b = self.find_parent(n.label)
                if a != b:
                    self.d[a] = b

        result = {}
        for k in self.d:
            key = self.find_parent(k)
            result[key] = result.get(key, []) + [k]

        # Not sure why the result must be sorted to pass... Maybe set?
        return sorted([sorted(i) for i in result.values()])

    def find_parent(self, n):
        if self.d[n] is not None:
            return self.find_parent(self.d[n])
        return n