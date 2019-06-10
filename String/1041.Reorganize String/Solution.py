from collections import defaultdict
import operator

class Solution:
    """
    @param S: a string
    @return: return a string
    """
    def reorganizeString(self, S):
        # write your code here
        if not S or len(S) == 0:
            return S

        count = defaultdict(int)
        for s in S:
            count[s] += 1

        length = len(S)
        ch, freq = max(count.items(), key=operator.itemgetter(1))
        if 2 * freq - length > 1:
            return ""

        S = sorted(S)
        result, total = [], 0
        for s in S:
            if s != ch:
                if total < freq:
                    result.append(ch)
                    total += 1
                result.append(s)

        if total < freq:
            result.append(ch)
            total += 1

        return "".join(result)
