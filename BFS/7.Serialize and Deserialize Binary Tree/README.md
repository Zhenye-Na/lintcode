# 7. Serialize and Deserialize Binary Tree

**Description**

Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

**Example**

Example 1:

```
Input: {3,9,20,#,#,15,7}
Output: {3,9,20,#,#,15,7}
Explanation:
Binary tree {3,9,20,#,#,15,7}, denote the following structure:
	  3
	 / \
	9  20
	  /  \
	 15   7
it will be serialized {3,9,20,#,#,15,7}
```

Example 2:

```
Input: {1,2,3}
Output: {1,2,3}
Explanation:
Binary tree {1,2,3}, denote the following structure:
   1
  / \
 2   3
it will be serialized {1,2,3}
```

Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.

You can use other method to do serializaiton and deserialization.

**BFS**

- `serialize()` 采用bfs，对当前二叉树搜索，遍历vector，将当前节点左右儿子依次存入 vector，空节点需要删去。
- `deserialize()` 首先切割字符串，然后用 isLeftChild 标记是当前是左右儿子，数字转化为字符串，存为队列首节点的左右儿子。

```python
from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        self.queue = deque([])
        self.serialization = []

        if root is None:
            return "#"

        self.queue.append(root)
        while self.queue:
            node = self.queue.popleft()
            if node is not None:
                self.serialization.append(str(node.val))
            else:
                self.serialization.append("#")
            if node is not None:
                self.queue.append(node.left)
                self.queue.append(node.right)

        length = len(self.serialization)
        for i in range(length - 1, -1, -1):
            if self.serialization[i] == "#":
                self.serialization.pop(i)
            else:
                break

        self.serialization = ",".join(self.serialization)
        return self.serialization

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data[0] == '#':
            return None

        nodeList = data.split(",")
        nodeQueue = deque(nodeList)

        root = TreeNode(int(nodeQueue.popleft()))
        q = deque([root])
        isLeft = True

        while nodeQueue:
            ch = nodeQueue.popleft()
            if ch != '#':
                node = TreeNode(int(ch))
                q.append(node)
                if isLeft:
                    q[0].left = node
                else:
                    q[0].right = node
            if not isLeft:
                q.popleft()
            isLeft = not isLeft
        return root
```

**DFS**

用 `'#'` 将 node 隔开。很直接的解决。思路是分治法 (不是遍历)

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

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
```
