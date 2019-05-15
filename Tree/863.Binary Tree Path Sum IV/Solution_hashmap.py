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