from heapq import heappush, heappop


class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """

    def mergeNumber(self, numbers):
        # Write your code here
        if not numbers or len(numbers) == 0:
            return 0

        heap = []
        for num in numbers:
            heappush(heap, num)

        ans = 0
        while len(heap) >= 2:
            num1 = heappop(heap)
            num2 = heappop(heap)
            ans += num1 + num2
            heappush(heap, num1 + num2)

        return ans
