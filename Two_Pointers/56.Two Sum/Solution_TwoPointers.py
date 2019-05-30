class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 2:
            return [-1, -1]

        arg_nums = [x for x, y in sorted(enumerate(numbers), key = lambda x: x[1])]
        numbers.sort()
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return sorted([arg_nums[left], arg_nums[right]])
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
