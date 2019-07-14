class Solution:
    """
    @param arr: The array
    @return: yes or no
    """

    def judgingTriangle(self, arr):
        # Write your code here
        if not arr or len(arr) == 0:
            return "no"

        n = len(arr)
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    return "yes"
                else:
                    left += 1

        return "no"
