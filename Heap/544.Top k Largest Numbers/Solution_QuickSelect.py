class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        start = 0
        end = len(nums) - 1 
        index = self.partition(nums, start, end)

        while index != len(nums) - k:
            if index > len(nums) - k:
                end = index - 1 
                index = self.partition(nums, start, end)
            else:
                start = index + 1 
                index = self.partition(nums, start, end)

        result = nums[index:]
        result.sort()

        return result[::-1]
        
    def partition(self, A, start, end):
        index = start
        for i in range(start, end):
            if A[i] > A[end]:
                continue

            A[index], A[i] = A[i], A[index]
            index += 1 

        A[index], A[end] = A[end], A[index]
        return index