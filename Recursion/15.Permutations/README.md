# 15. Permutations

**Description**

Given a list of numbers, return all possible permutations.

You can assume that there is no duplicate numbers in the list.

**Example**

Example 1:

```
Input: [1]
Output:
[
  [1]
]
```

Example 2:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

**Challenge**

Do it without recursion.


**Challenge**

Do it without recursion.


**1. Backtracking**

```python
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [[]]

        nums.sort()
        permutations = []
        self._find_permutations(nums, permutations, [])
        return permutations

    def _find_permutations(self, nums, permutations, permutation):
        if len(permutation) == len(nums):
            permutations.append(permutation[:])
            return

        for num in nums:
            if num not in permutation:
                # add new element
                permutation.append(num)
                # explore
                self._find_permutations(nums, permutations, permutation)
                # remove last element
                permutation.pop()
```

**2. Non-Recursion**

```java
// Non-Recursion
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<List<Integer>> permutations
             = new ArrayList<List<Integer>>();
        if (nums == null) {
            return permutations;
        }

        if (nums.length == 0) {
            permutations.add(new ArrayList<Integer>());
            return permutations;
        }

        int n = nums.length;
        ArrayList<Integer> stack = new ArrayList<Integer>();
        
        stack.add(-1);
        while (stack.size() != 0) {
            Integer last = stack.get(stack.size() - 1);
            stack.remove(stack.size() - 1);

            // increase the last number
            int next = -1;
            for (int i = last + 1; i < n; i++) {
                if (!stack.contains(i)) {
                    next = i;
                    break;
                }
            }
            if (next == -1) {
                continue;
            }

            // generate the next permutation
            stack.add(next);
            for (int i = 0; i < n; i++) {
                if (!stack.contains(i)) {
                    stack.add(i);
                }
            }

            // copy to permutations set
            ArrayList<Integer> permutation = new ArrayList<Integer>();
            for (int i = 0; i < n; i++) {
                permutation.add(nums[stack.get(i)]);
            }
            permutations.add(permutation);
        }

        return permutations;
    }
}
```

**3. `itertools.permutations()`**

(我知道有这个包, 我可以用不? 嘻嘻嘻)

```python
import itertools

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        return list(itertools.permutations(nums))
```
