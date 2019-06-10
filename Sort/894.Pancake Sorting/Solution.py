class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        if not array or len(array) == 0:
            return

        n = len(array)
        for i in range(n - 1, -1, -1):
            max_idx = self.findMax(array[: i + 1])
            if max_idx != i:
                FlipTool.flip(array, max_idx)
                FlipTool.flip(array, i)

    def findMax(self, array):
        max_num, max_idx = - sys.maxsize, -1
        for i in range(len(array)):
            if array[i] > max_num:
                max_idx = i
                max_num = array[i]

        return max_idx
