# 863. Binary Tree Path Sum IV

**Description**

If the depth of a tree is smaller than `5`, this tree can be represented by a list of three-digits integers.

For each integer in this list:

```
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.
```

**Example**

Example 1:
```
Input: [113, 215, 221]
Output: 12
Explanation:
  The tree that the list represents is:
    3
   / \
  5   1
  The path sum is (3 + 5) + (3 + 1) = 12.
```

Example 2:

```
Input: [113, 221]
Output: 4
Explanation:
  The tree that the list represents is:
    3
     \
      1
  The path sum is 3 + 1 = 4.
```

**Hash Map**

简单讲就是将每个数的前两位数作为 `unique key`, 将其个位数作为 `value`, 放入 hashmap中, 因此有

- `depth = key // 10`, `pos = key % 10`
- `left_child_key = (depth + 1) * 10 + pos * 2 - 1`
- `right_child_key = left_child_key + 1`

最后采用 dfs 直接求解

```python
class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """
    def pathSum(self, nums):
        # write your code here
        if not nums or len(nums) > 15:
            return 0
        nums.sort()
        mapping = self._create_mapping(nums)
        root_pos = int(nums[0]) // 10

        self.path_sum = 0
        self._dfs(root_pos, mapping, 0)
        return self.path_sum


    def _create_mapping(self, nums):
        mapping = {}
        for node in nums:
            node_pos = int(node) // 10
            node_val = int(node) % 10
            mapping[node_pos] = node_val

        return mapping


    def _dfs(self, root_pos, mapping, current_sum):
        if root_pos not in mapping:
            return

        current_sum += mapping[root_pos]

        depth = root_pos // 10 + 1
        left = (root_pos % 10) * 2 - 1
        right = (root_pos % 10) * 2

        root_pos_left = depth * 10 + left
        root_pos_right = depth * 10 + right

        self._dfs(root_pos_left, mapping, current_sum)
        self._dfs(root_pos_right, mapping, current_sum)

        if root_pos_left not in mapping and root_pos_right not in mapping:
            self.path_sum += current_sum
            return
```


**2D Array**

上一种方法是用 HashMap 来记录每一个 TreeNode 的位置, 然后做DFS.

还可以考虑用二维数组保存这棵树, 很容易根据列表解析出来这棵二叉树.

行代表深度, 列代表具体位置

```python
class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """

    def pathSum(self, nums):
        n, siz = len(nums), 1
        self.ans, self.mx = 0, nums[n - 1] // 100

        for i in range(self.mx - 1):
            siz *= 2
        g = [[-1 for j in range(siz)]for i in range(self.mx)]

        for i in range(n):
            dep, pos = nums[i] // 100, nums[i] // 10 % 10
            g[dep - 1][pos - 1] = nums[i] % 10
        self.dfs(g, 0, 0, 0)

        return self.ans

    def dfs(self, g, d, p, sum):
        if(g[d][p] == -1):
            return

        sum += g[d][p]
        if (d == self.mx - 1 or (g[d + 1][2 * p] == -1 and g[d + 1][2 * p + 1] == -1)):
            self.ans += sum
            return

        self.dfs(g, d + 1, 2 * p, sum)
        self.dfs(g, d + 1, 2 * p + 1, sum)
```