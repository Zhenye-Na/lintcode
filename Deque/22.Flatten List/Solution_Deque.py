from collections import deque

class Solution(object):

    # @param nestedList a list, each element in the list can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if not nestedList or len(nestedList) == 0:
            return nestedList

        queue = deque(nestedList)
        res = []
        while queue:
            ele = queue.popleft()
            if isinstance(ele, list):
                for e in reversed(ele):
                    queue.appendleft(e)
            else:
                res.append(ele)

        return res
