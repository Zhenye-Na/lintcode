class Solution:

    def serialize(self, root):
        # write your code here
        if not root:
            return ['#']
        ans = []
        ans.append(str(root.val))
        ans += self.serialize(root.left)
        ans += self.serialize(root.right)
        return ans

    def deserialize(self, data):
        # write your code here
        ch = data.pop(0)
        if ch == '#':
            return None
        else:
            root = TreeNode(int(ch))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root


class Solution:

    def serialize(self, root):
        if not root:
            return ['#']
        return [str(root.val)] + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        elem = data.pop(0)
        if elem == '#':
            return None
        root = TreeNode(int(elem))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
