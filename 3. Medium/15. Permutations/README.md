# 15. Permutations

- **Description**
    - Given a list of numbers, return all possible permutations.
    - You can assume that there is no duplicate numbers in the list.
- **Example**
    - For `nums = [1,2,3]`, the permutations are:

    ```
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    ```

- **Challenge**
    - Do it without recursion.

## Solution


### Backtracking

```python
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def __init__(self):
        self.results = []
        self.length = 0

    def permute(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            self.results.append([])
            return self.results

        self.length = len(nums)
        self.backtracking(0, nums, [])
        return self.results


    def backtracking(self, startIndex, nums, permutation):
        if len(permutation) == len(nums):
            self.results.append(permutation[:])
            return

        for idx in xrange(startIndex, self.length):

            if nums[idx] in permutation:
                continue

            # add new element
            permutation.append(nums[idx])

            # explore
            self.backtracking(0, nums, permutation)

            # remove element
            permutation.pop(-1)

```
