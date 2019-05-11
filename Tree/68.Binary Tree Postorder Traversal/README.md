# 68. Binary Tree Postorder Traversal

**Description**

Given a binary tree, return the postorder traversal of its nodes' values.

```
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
```

**Example**

Example 1:

```
Input：{1,2,3}
Output：[2,3,1]
Explanation:  
   1
  / \
 2   3
it will be serialized {1,2,3}
Post order traversal
```

Example 2:

```
Input：{1,#,2,3}
Output：[3,2,1]
Explanation:  
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Post order traversal
```

**Challenge**

Can you do it without recursion?


**Non-Recursion: One Stack**

[Iterative Postorder traversal of binary tree using one stack - Tushar](https://www.youtube.com/watch?v=xLQKdq0Ffjg)

code sample in the video

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        current = root
        stack = []
        result = []

        while current is not None or len(stack) != 0:

            if current is not None:
                stack.append(current)
                current = current.left

            else:
                tmp = stack[-1].right

                if tmp is None:
                    tmp = stack.pop()
                    result.append(tmp.val)

                    while len(stack) != 0 and tmp == stack[-1].right:
                        tmp = stack.pop()
                        result.append(tmp.val)
                
                else:
                    current = tmp

        return result
```

第二种解 - one stack

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        stack  = []

        if root is None:
            return result

        stack.append(root)
        while stack:
            node = stack.pop()
            result.insert(0, node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result
```


**Iterative Postorder Traversal of Binary Tree with Two Stacks**


[Iterative Postorder Traversal of Binary Tree - YouTube by Tushar](https://www.youtube.com/watch?v=qT65HltK2uE)

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result

        # Initialize two stacks
        s1 = []
        s2 = []

        s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        # pop stack2 to get postorder traversal
        while s2:
            result.append(s2.pop().val)

        return result
```



**Traverse helper function**

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None:
            return

        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)
```



**Divide & Conquer**

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```
