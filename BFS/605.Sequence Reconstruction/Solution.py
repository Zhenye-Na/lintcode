from collections import deque, defaultdict

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if not seqs or len(seqs) == 0 :
            return False

        unqiue_seqs = [item for sublist in seqs for item in sublist]
        unique_seqs = list(set(unqiue_seqs))
        unique_seqs.sort()
        unique_orgs = list(set(org))
        unique_orgs.sort()
        if unique_seqs != unique_orgs:
            return False

        neighbors = self._getNeighbors(seqs)
        indegree = self._getIndegrees(neighbors, org)

        start_nums = [num for num in org if indegree[num] == 0]
        queue = deque(start_nums)
        reconstruction = []

        while queue:

            if len(queue) > 1:
                # there must exist more than one topo orders
                return False

            num = queue.popleft()
            reconstruction.append(num)

            for neighbor in neighbors[num]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return len(reconstruction) == len(org) and reconstruction == org 


    def _getNeighbors(self, seqs):
        neighbors = defaultdict(set)

        for seq in seqs:
            for i in range(1, len(seq)):
                neighbors[seq[i - 1]].add(seq[i])

        return neighbors


    def _getIndegrees(self, neighbors, org):
        indegrees = defaultdict(int)

        for node in org:
            for neighbor in neighbors[node]:
                indegrees[neighbor] += 1
                
        return indegrees
