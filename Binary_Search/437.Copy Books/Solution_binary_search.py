class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages or len(pages) == 0 or not k or k == 0:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._compute_k(pages, mid) > k:
                start = mid
            else:
                end = mid

        if self._compute_k(pages, start) <= k:
            return start
        else:
            return end



    def _compute_k(self, pages, target):
        worker = 1
        time = 0
        for i in range(len(pages)):
            if time + pages[i] > target:
                time = pages[i]
                worker += 1
            else:
                time += pages[i]

        return worker
