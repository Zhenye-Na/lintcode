from collections import defaultdict


class Solution:
    """
    @param list_of_set: Initial list of set
    @return: The final number of sets
    """
    def setUnion(self, list_of_set):
        # Write your code here
        if not list_of_set or len(list_of_set) == 0:
            return 0

        self.forward_dict = self._create_forward(list_of_set)
        self.backward_dict = self._create_backward(list_of_set)

        self.parents = {k : k for k in range(len(list_of_set))}

        for elem, idx in self.backward_dict.items():
            if len(idx) > 0:
                first = idx[0]
                for i in range(1, len(idx)):
                    self._union(first, idx[i])

        count = 0
        for idx, elem in self.forward_dict.items():
            if len(elem) > 0:
                count += 1

        return count


    def _create_forward(self, list_of_set):
        forward = defaultdict(set)
        for idx, s in enumerate(list_of_set):
            forward[idx].add(tuple(s))
        return forward

    def _create_backward(self, list_of_set):
        backward = defaultdict(list)
        for idx, set_list in enumerate(list_of_set):
            for elem in set_list:
                backward[elem].append(idx)
        return backward

    def _union(self, e1, e2):
        root_1 = self._find(e1)
        root_2 = self._find(e2)
        if root_1 != root_2:
            self.parents[root_1] = root_2
            self.forward_dict[root_2].union(self.forward_dict[root_1])
            self.forward_dict[root_1].clear()

    def _find(self, elem):
        path = []
        while elem != self.parents[elem]:
            path.append(elem)
            elem = self.parents[elem]

        for e in path:
            self.parents[e] = elem

        return elem
