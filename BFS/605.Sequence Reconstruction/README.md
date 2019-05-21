# 605. Sequence Reconstruction

**Description**

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

**Example**

Example 1:

```
Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
```

Example 2:

```
Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2].
```

Example 3:

```
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
```

Example 4:

```
Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true
```

**BFS**

保证 `queue` 中最多同时存在 `1` 个元素即可

```python
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
```