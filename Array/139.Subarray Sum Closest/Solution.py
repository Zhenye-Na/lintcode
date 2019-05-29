class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return -1, -1

        prefix_sum = 0
        prefix_list = [(0, -1)]

        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_list.append((prefix_sum, i))

        prefix_list.sort(key=lambda x : x[0])

        min_diff = sys.maxsize
        l, r = -1, -1
        for i in range(1, len(prefix_list)):
            diff = prefix_list[i][0] - prefix_list[i - 1][0]
            if diff < min_diff:
                min_diff = diff
                l = min(prefix_list[i][1], prefix_list[i - 1][1]) + 1
                r = max(prefix_list[i][1], prefix_list[i - 1][1])

        return l, r
