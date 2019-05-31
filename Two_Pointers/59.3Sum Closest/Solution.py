class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 3:
            return 0

        numbers.sort()
        self.ans = sys.maxsize
        for i in range(len(numbers)):
            self._twoSumCloset(numbers, i + 1, len(numbers) - 1, numbers[i], target)

        return self.ans

    def _twoSumCloset(self, nums, left, right, c, target):
        while left < right:
            total = nums[left] + nums[right] + c
            if abs(total - target) < abs(self.ans - target):
                self.ans = total

            if total < target:
                left += 1
            else:
                right -= 1
