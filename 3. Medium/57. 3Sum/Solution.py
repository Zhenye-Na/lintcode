class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        numbers.sort()

        for index, elem in enumerate(numbers):

            # Remove duplicate elements in the front
            if (index > 0 and numbers[index - 1] == elem):
                continue

            start, end = index + 1, len(numbers) - 1
            while start < end:

                if (numbers[start] + numbers[end] + elem > 0):
                    end -= 1
                elif (numbers[start] + numbers[end] + elem < 0):
                    start += 1
                else:
                    # Append one possible combination
                    result.append([elem, numbers[start], numbers[end]])

                    # Move pointers
                    start += 1
                    end -= 1

                    # Remove duplicates
                    while (start < end and numbers[start] == numbers[start - 1]):
                        start += 1
                    while (start < end and numbers[end] == numbers[end + 1]):
                        end -= 1

        return result
