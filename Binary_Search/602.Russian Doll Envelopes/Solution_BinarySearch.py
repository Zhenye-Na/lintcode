from bisect import bisect_left

class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        if not envelopes or len(envelopes) == 0:
            return 0

        sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        
        lis, length = [0 for _ in range(len(envelopes))], 0
        for w, h in sorted_envelopes:
            idx = bisect_left(lis, h, 0, length)
            lis[idx] = h

            if idx == length:
                length += 1

        return length
